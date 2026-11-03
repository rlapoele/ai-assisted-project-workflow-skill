#!/usr/bin/env python3
"""Install a copy or development link without silently overwriting local work."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil


SKILL_NAME = "manage-ai-assisted-projects"


def install(source, skills_dir, *, replace=False, link=False):
    source = Path(source).resolve()
    skills_dir = Path(skills_dir).expanduser().resolve()
    destination = skills_dir / SKILL_NAME
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source does not contain SKILL.md")
    if (destination == source or skills_dir == source or source in skills_dir.parents
            or (not destination.is_symlink() and destination in source.parents)):
        raise ValueError("Installation destination must be outside the source skill")
    if destination.exists() and destination.resolve() == source and not link:
        # Replacing an existing development link with a copy is supported.
        if not destination.is_symlink():
            raise ValueError("Refusing to replace the source skill")
    exists = destination.exists() or destination.is_symlink()
    if exists and not replace:
        raise FileExistsError(f"{destination} already exists; use --replace to back it up")
    backup = None
    original_link = destination.readlink() if destination.is_symlink() else None
    original_link_destination = destination.resolve() if original_link is not None else None
    skills_dir.mkdir(parents=True, exist_ok=True)
    if exists:
        backup_dir = skills_dir.parent / (skills_dir.name + "-backups")
        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = backup_dir / f"{SKILL_NAME}-{stamp}"
        destination.rename(backup)
    try:
        if backup is not None and original_link is not None:
            # A relative symlink must keep pointing at the original target after moving.
            backup.unlink()
            backup.symlink_to(original_link_destination, target_is_directory=True)
        if link:
            destination.symlink_to(source, target_is_directory=True)
        else:
            shutil.copytree(source, destination)
    except Exception:
        # Remove only output created by this attempt, then restore the old install.
        if destination.is_symlink():
            destination.unlink()
        elif destination.exists():
            shutil.rmtree(destination)
        if backup is not None:
            if original_link is not None:
                if backup.is_symlink():
                    backup.unlink()
                destination.symlink_to(original_link, target_is_directory=True)
            else:
                backup.rename(destination)
        raise
    return destination, backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--replace", action="store_true", help="Back up and replace an existing installation")
    parser.add_argument("--link", action="store_true", help="Link to source instead of copying")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / SKILL_NAME
    try:
        destination, backup = install(source, args.skills_dir, replace=args.replace, link=args.link)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")
    print(f"Installed {'link' if args.link else 'copy'}: {destination}")
    if backup is not None:
        print(f"Previous installation preserved at: {backup}")


if __name__ == "__main__":
    main()
