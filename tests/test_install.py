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
        self.assertTrue(backup.is_symlink())
        self.assertEqual((self.source / "SKILL.md").read_text(), "updated\n")

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

    def test_relative_link_backup_preserves_original_target(self):
        self.skills.mkdir(parents=True)
        target = self.skills / installer.SKILL_NAME
        target.symlink_to("../../source", target_is_directory=True)
        target, backup = installer.install(self.source, self.skills, replace=True)
        self.assertEqual((backup / "SKILL.md").read_text(), "original skill\n")
        self.assertEqual(backup.resolve(), self.source.resolve())
        self.assertFalse(target.is_symlink())

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
