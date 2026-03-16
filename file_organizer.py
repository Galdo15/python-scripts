"""
file_organizer.py
-----------------
Automatically organizes files in a folder by their extension.
Creates subfolders for each file type and moves files accordingly.

Author: Jose Alvarez
Project: Portfolio - File Automation Scripts
"""

import os
import shutil


# --- Configuration ---
# Change this path to the folder you want to organize
TARGET_FOLDER = os.path.expanduser("~/Downloads")

# Custom category mapping: folder name -> list of extensions
CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Audio":      [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xlsx", ".xls", ".csv", ".ods"],
    "Slides":     [".pptx", ".ppt", ".odp"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".cpp", ".ts", ".json", ".sql"],
    "Archives":   [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables":[".exe", ".msi", ".dmg", ".pkg", ".sh"],
}


def get_category(extension: str) -> str:
    """Return the category folder name for a given file extension."""
    ext_lower = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext_lower in extensions:
            return category
    return "Other"


def organize_folder(folder_path: str) -> dict:
    """
    Organize all files in the given folder into subfolders by category.
    Returns a summary dict: { category: count_of_files_moved }
    """
    if not os.path.isdir(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return {}

    summary = {}
    skipped = 0

    print(f"\n📂 Organizing: {folder_path}\n")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip subfolders and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            skipped += 1
            continue

        # Determine category
        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        # Create destination folder if it doesn't exist
        dest_folder = os.path.join(folder_path, category)
        os.makedirs(dest_folder, exist_ok=True)

        # Handle filename conflicts
        dest_path = os.path.join(dest_folder, filename)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

        # Move the file
        shutil.move(file_path, dest_path)
        print(f"  ✅ {filename}  →  {category}/")

        summary[category] = summary.get(category, 0) + 1

    # Print summary
    print("\n--- Summary ---")
    for category, count in sorted(summary.items()):
        print(f"  {category}: {count} file(s)")
    if skipped:
        print(f"  Skipped (folders/hidden): {skipped}")
    print(f"\nDone! {sum(summary.values())} file(s) organized.\n")

    return summary


if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)
