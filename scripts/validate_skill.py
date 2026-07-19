#!/usr/bin/env python3
"""Validate SKILL.md files: YAML frontmatter with name and description,
name matching the parent folder, non-empty description. Stdlib only."""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(text: str) -> dict | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip("'\"")
    return None  # closing --- never found


def validate(skill_md: Path) -> list[str]:
    errors = []
    fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fm is None:
        return [f"{skill_md}: missing or unterminated YAML frontmatter (--- ... ---)"]
    name = fm.get("name")
    if not name:
        errors.append(f"{skill_md}: frontmatter is missing 'name'")
    elif name != skill_md.parent.name:
        errors.append(
            f"{skill_md}: name '{name}' does not match folder '{skill_md.parent.name}'"
        )
    if not fm.get("description"):
        errors.append(f"{skill_md}: frontmatter is missing a non-empty 'description'")
    return errors


def main() -> int:
    skill_files = sorted(REPO_ROOT.glob("*/SKILL.md"))
    if not skill_files:
        print("ERROR: no SKILL.md found in any top-level folder")
        return 1
    all_errors = []
    for skill_md in skill_files:
        errors = validate(skill_md)
        rel = skill_md.relative_to(REPO_ROOT)
        if errors:
            all_errors.extend(errors)
            print(f"FAIL {rel}")
        else:
            print(f"OK   {rel}")
    for error in all_errors:
        print(f"ERROR: {error}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
