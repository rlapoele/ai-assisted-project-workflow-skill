import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "scripts" / "install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        (self.source / "SKILL.md").write_text("original skill\n")
        (self.source / "references").mkdir()
        (self.source / "references" / "guide.md").write_text("guide\n")
        self.skills = self.root / "client" / "skills"

    def test_copy_is_independent_and_refuses_silent_overwrite(self):
        target, backup = installer.install(self.source, self.skills)
        self.assertIsNone(backup)
        self.assertEqual((target / "references" / "guide.md").read_text(), "guide\n")
        (target / "SKILL.md").write_text("local edits\n")
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.skills)
        self.assertEqual((target / "SKILL.md").read_text(), "local edits\n")
        self.assertEqual((self.source / "SKILL.md").read_text(), "original skill\n")

    def test_replace_preserves_old_content_outside_discovery(self):
        target, _ = installer.install(self.source, self.skills)
        (target / "SKILL.md").write_text("local edits\n")
        target, backup = installer.install(self.source, self.skills, replace=True)
        self.assertNotEqual(backup.parent, self.skills)
        self.assertEqual((backup / "SKILL.md").read_text(), "local edits\n")
        self.assertEqual((target / "SKILL.md").read_text(), "original skill\n")

    def test_link_follows_source_and_can_be_replaced_with_copy(self):
        target, _ = installer.install(self.source, self.skills, link=True)
        self.assertTrue(target.is_symlink())
        (self.source / "SKILL.md").write_text("updated\n")
        self.assertEqual((target / "SKILL.md").read_text(), "updated\n")
        target, backup = installer.install(self.source, self.skills, replace=True)
        self.assertFalse(target.is_symlink())
        self.assertFalse(backup.is_symlink())
        self.assertEqual((self.source / "SKILL.md").read_text(), "updated\n")
        (self.source / "SKILL.md").write_text("changed after replacement\n")
        self.assertEqual((backup / "SKILL.md").read_text(), "updated\n")

    def test_failed_replacement_restores_previous_install(self):
        target, _ = installer.install(self.source, self.skills)
        (target / "SKILL.md").write_text("keep me\n")
        with patch.object(installer.shutil, "copytree", side_effect=OSError("simulated failure")):
            with self.assertRaises(OSError):
                installer.install(self.source, self.skills, replace=True)
        self.assertEqual((target / "SKILL.md").read_text(), "keep me\n")

    def test_source_cannot_be_replaced_or_copied_into_itself(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / "nested", replace=True)
        self.assertEqual((self.source / "SKILL.md").read_text(), "original skill\n")

    def test_relative_link_backup_snapshots_contents(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to("../../source", target_is_directory=True)
        target, backup = installer.install(self.source, self.skills, replace=True)
        self.assertEqual((backup / "SKILL.md").read_text(), "original skill\n")
        self.assertFalse(backup.is_symlink())
        (self.source / "SKILL.md").unlink()
        self.assertEqual((backup / "SKILL.md").read_text(), "original skill\n")
        self.assertFalse(target.is_symlink())

    def test_link_snapshot_dereferences_nested_links(self):
        external = self.root / "external.txt"
        external.write_text("original external content\n")
        (self.source / "reference.txt").symlink_to(external)
        installer.install(self.source, self.skills, link=True)
        _, backup = installer.install(self.source, self.skills, replace=True, link=True)
        external.unlink()
        self.assertFalse((backup / "reference.txt").is_symlink())
        self.assertEqual((backup / "reference.txt").read_text(), "original external content\n")

    def test_partial_snapshot_failure_leaves_original_link_untouched(self):
        target, _ = installer.install(self.source, self.skills, link=True)

        def partial_copy(source, destination, **kwargs):
            Path(destination).mkdir()
            (Path(destination) / "partial.txt").write_text("incomplete\n")
            raise OSError("snapshot failed")

        with patch.object(installer.shutil, "copytree", side_effect=partial_copy):
            with self.assertRaises(OSError):
                installer.install(self.source, self.skills, replace=True)
        self.assertTrue(target.is_symlink())
        self.assertEqual((target / "SKILL.md").read_text(), "original skill\n")
        self.assertEqual(list((self.skills.parent / "skills-backups").iterdir()), [])

    def test_failed_install_after_snapshot_restores_relative_link(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to("../../source", target_is_directory=True)
        real_copytree = installer.shutil.copytree

        def fail_install(source, destination, *args, **kwargs):
            if Path(destination).resolve() == target.resolve():
                Path(destination).mkdir()
                (Path(destination) / "partial.txt").write_text("incomplete\n")
                raise OSError("replacement failed")
            return real_copytree(source, destination, *args, **kwargs)

        with patch.object(installer.shutil, "copytree", side_effect=fail_install):
            with self.assertRaises(OSError):
                installer.install(self.source, self.skills, replace=True)
        self.assertEqual(str(target.readlink()), "../../source")
        backups = list((self.skills.parent / "skills-backups").iterdir())
        self.assertEqual(len(backups), 1)
        self.assertFalse(backups[0].is_symlink())
        self.assertEqual((backups[0] / "SKILL.md").read_text(), "original skill\n")

    def test_dangling_link_replacement_refuses_without_removing_link(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to("missing-target", target_is_directory=True)
        with self.assertRaises(OSError):
            installer.install(self.source, self.skills, replace=True)
        self.assertEqual(str(target.readlink()), "missing-target")

    def test_broken_nested_link_prevents_snapshot_before_replacement(self):
        (self.source / "missing.txt").symlink_to("absent.txt")
        target, _ = installer.install(self.source, self.skills, link=True)
        with self.assertRaises(OSError):
            installer.install(self.source, self.skills, replace=True)
        self.assertTrue(target.is_symlink())
        self.assertEqual((target / "SKILL.md").read_text(), "original skill\n")
        self.assertEqual(list((self.skills.parent / "skills-backups").iterdir()), [])

    def test_refuses_backup_directory_redirected_into_discovery(self):
        target, _ = installer.install(self.source, self.skills)
        (self.skills.parent / "skills-backups").symlink_to(self.skills, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(self.source, self.skills, replace=True)
        self.assertEqual((target / "SKILL.md").read_text(), "original skill\n")

    def test_link_snapshot_refuses_backup_inside_original_target(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to(self.skills.parent, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(self.source, self.skills, replace=True)
        self.assertTrue(target.is_symlink())

    def test_nested_link_cannot_reach_backup_or_form_a_cycle(self):
        backup_dir = self.skills.parent / "skills-backups"
        backup_dir.mkdir(parents=True)
        for linked_target in (backup_dir, self.source):
            with self.subTest(target=linked_target.name):
                nested = self.source / "nested"
                nested.symlink_to(linked_target, target_is_directory=True)
                target, _ = installer.install(self.source, self.skills, link=True)
                real_copytree = installer.shutil.copytree
                calls = 0

                def bounded_copy(*args, **kwargs):
                    nonlocal calls
                    calls += 1
                    if calls > 6:
                        raise RuntimeError("bounded probe stopped recursive snapshot")
                    return real_copytree(*args, **kwargs)

                with patch.object(installer.shutil, "copytree", side_effect=bounded_copy):
                    with self.assertRaises(ValueError):
                        installer.install(self.source, self.skills, replace=True)
                self.assertTrue(target.is_symlink())
                self.assertEqual(list(backup_dir.iterdir()), [])
                target.unlink()
                nested.unlink()

    def test_failed_replacement_restores_relative_link(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to("../../source", target_is_directory=True)
        with patch.object(installer.shutil, "copytree", side_effect=OSError("simulated failure")):
            with self.assertRaises(OSError):
                installer.install(self.source, self.skills, replace=True)
        self.assertEqual(str(target.readlink()), "../../source")
        self.assertEqual((target / "SKILL.md").read_text(), "original skill\n")

    def test_rejects_source_nested_in_destination_before_mutation(self):
        target = self.skills / installer.SKILL_NAME
        nested = target / "source"
        nested.mkdir(parents=True)
        (nested / "SKILL.md").write_text("nested source\n")
        for link in (False, True):
            with self.subTest(link=link):
                with self.assertRaises(ValueError):
                    installer.install(nested, self.skills, replace=True, link=link)
        self.assertFalse(target.is_symlink())
        self.assertEqual((nested / "SKILL.md").read_text(), "nested source\n")
        self.assertFalse((self.skills.parent / "skills-backups").exists())


if __name__ == "__main__":
    unittest.main()
