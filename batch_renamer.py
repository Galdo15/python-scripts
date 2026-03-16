"""
batch_renamer.py
----------------
Batch rename files in a folder with flexible options:
  - Add a prefix or suffix
  - Replace text in filenames
  - Number files sequentially
  - Change extension case

Includes a dry-run mode to preview changes before applying them.

Author: Jose Alvarez
Project: Portfolio - File Automation Scripts
"""

import os
import argparse


def get_files(folder: str, extension_filter: str = None) -> list:
    """Return a sorted list of filenames in the folder (files only)."""
    all_files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f)) and not f.startswith(".")
    ]
    if extension_filter:
        ext = extension_filter.lower()
        all_files = [f for f in all_files if f.lower().endswith(ext)]
    return sorted(all_files)


def build_new_name(
    filename: str,
    index: int,
    prefix: str = "",
    suffix: str = "",
    find: str = "",
    replace: str = "",
    sequential: bool = False,
    start: int = 1,
    padding: int = 3,
    lower_ext: bool = False,
) -> str:
    """Build the new filename based on the selected options."""
    name, ext = os.path.splitext(filename)

    # Replace text inside the name
    if find:
        name = name.replace(find, replace)

    # Add prefix and suffix
    name = f"{prefix}{name}{suffix}"

    # Sequential numbering (replaces the name entirely with a number)
    if sequential:
        number = str(index + start - 1).zfill(padding)
        name = f"{prefix}{number}{suffix}"

    # Normalize extension case
    if lower_ext:
        ext = ext.lower()

    return f"{name}{ext}"


def batch_rename(
    folder: str,
    extension_filter: str = None,
    prefix: str = "",
    suffix: str = "",
    find: str = "",
    replace: str = "",
    sequential: bool = False,
    start: int = 1,
    padding: int = 3,
    lower_ext: bool = False,
    dry_run: bool = True,
) -> None:
    """
    Rename files in the folder according to the given options.
    If dry_run=True, only shows a preview without renaming anything.
    """
    if not os.path.isdir(folder):
        print(f"[ERROR] Folder not found: {folder}")
        return

    files = get_files(folder, extension_filter)

    if not files:
        print("No files found matching the criteria.")
        return

    mode_label = "🔍 DRY RUN (preview only)" if dry_run else "✏️  RENAMING FILES"
    print(f"\n{mode_label}\nFolder: {folder}\n")
    print(f"  {'Original':<40} →  New Name")
    print(f"  {'-'*40}    {'-'*40}")

    renamed = 0
    skipped = 0

    for index, filename in enumerate(files, start=1):
        new_name = build_new_name(
            filename, index,
            prefix=prefix, suffix=suffix,
            find=find, replace=replace,
            sequential=sequential, start=start,
            padding=padding, lower_ext=lower_ext,
        )

        if new_name == filename:
            skipped += 1
            continue

        print(f"  {filename:<40} →  {new_name}")

        if not dry_run:
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, new_name)
            if os.path.exists(dst):
                print(f"    ⚠️  Skipped (destination already exists): {new_name}")
                skipped += 1
                continue
            os.rename(src, dst)

        renamed += 1

    print(f"\n  Files to rename: {renamed} | Unchanged: {skipped}")
    if dry_run:
        print("  Run with --apply to execute the rename.\n")
    else:
        print(f"  ✅ Done! {renamed} file(s) renamed.\n")


# --- CLI Interface ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Batch rename files in a folder."
    )
    parser.add_argument("folder", help="Path to the target folder")
    parser.add_argument("--ext",        default=None,  help="Filter by extension (e.g. .jpg)")
    parser.add_argument("--prefix",     default="",    help="Add a prefix to filenames")
    parser.add_argument("--suffix",     default="",    help="Add a suffix before the extension")
    parser.add_argument("--find",       default="",    help="Text to find in filenames")
    parser.add_argument("--replace",    default="",    help="Replacement text")
    parser.add_argument("--sequential", action="store_true", help="Number files sequentially")
    parser.add_argument("--start",      type=int, default=1, help="Starting number (default: 1)")
    parser.add_argument("--padding",    type=int, default=3, help="Zero-padding digits (default: 3)")
    parser.add_argument("--lower-ext",  action="store_true", help="Convert extension to lowercase")
    parser.add_argument("--apply",      action="store_true", help="Actually rename files (default is dry run)")

    args = parser.parse_args()

    batch_rename(
        folder=args.folder,
        extension_filter=args.ext,
        prefix=args.prefix,
        suffix=args.suffix,
        find=args.find,
        replace=args.replace,
        sequential=args.sequential,
        start=args.start,
        padding=args.padding,
        lower_ext=args.lower_ext,
        dry_run=not args.apply,
    )


# --- Quick usage examples (run in terminal) ---
#
# Preview renaming all files with prefix "2025_":
#   python batch_renamer.py ~/Photos --prefix "2025_"
#
# Actually apply it:
#   python batch_renamer.py ~/Photos --prefix "2025_" --apply
#
# Rename only .jpg files sequentially (001, 002, ...):
#   python batch_renamer.py ~/Photos --ext .jpg --sequential --apply
#
# Replace spaces with underscores:
#   python batch_renamer.py ~/Documents --find " " --replace "_" --apply
