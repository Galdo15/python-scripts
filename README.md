# 🐍 Python Automation Scripts

A collection of Python scripts for file management and automation tasks.
Built to be simple, practical, and easy to customize.

---

## 📁 Scripts

### 1. `file_organizer.py` — Automatic File Organizer

Automatically sorts all files in a folder into subfolders by file type.

**Categories it creates:**
| Folder | File Types |
|---|---|
| Images | .jpg, .png, .gif, .svg, .webp … |
| Videos | .mp4, .mov, .avi, .mkv … |
| Documents | .pdf, .docx, .txt, .odt … |
| Code | .py, .js, .html, .css, .sql … |
| Archives | .zip, .rar, .tar, .gz … |
| + more | Spreadsheets, Audio, Executables |

**How to use:**
```bash
# 1. Open the file and set your target folder
TARGET_FOLDER = "/your/folder/path"

# 2. Run it
python file_organizer.py
```

**Example output:**
```
📂 Organizing: /Users/jose/Downloads

  ✅ report.pdf        →  Documents/
  ✅ photo.jpg         →  Images/
  ✅ script.py         →  Code/
  ✅ archive.zip       →  Archives/

--- Summary ---
  Code: 3 file(s)
  Documents: 5 file(s)
  Images: 12 file(s)

Done! 20 file(s) organized.
```

---

### 2. `batch_renamer.py` — Batch File Renamer

Rename multiple files at once with flexible options.
Includes a **dry run mode** — preview all changes before applying them.

**Options:**
| Flag | Description | Example |
|---|---|---|
| `--prefix` | Add text before filename | `--prefix "2025_"` |
| `--suffix` | Add text before extension | `--suffix "_final"` |
| `--find` / `--replace` | Replace text in filenames | `--find " " --replace "_"` |
| `--sequential` | Number files (001, 002…) | `--sequential` |
| `--ext` | Filter by extension only | `--ext .jpg` |
| `--apply` | Apply changes (default: dry run) | `--apply` |

**How to use:**
```bash
# Preview first (dry run — nothing is changed)
python batch_renamer.py ~/Photos --prefix "2025_"

# Apply when ready
python batch_renamer.py ~/Photos --prefix "2025_" --apply

# Rename only .jpg files sequentially
python batch_renamer.py ~/Photos --ext .jpg --sequential --apply

# Replace spaces with underscores
python batch_renamer.py ~/Documents --find " " --replace "_" --apply
```

---

## ⚙️ Requirements

- Python 3.6+
- No external libraries needed (uses only built-in modules)

```bash
python --version  # Make sure you have Python 3.6+
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/python-scripts.git
cd python-scripts

# Run any script directly
python file_organizer.py
python batch_renamer.py --help
```

---

## 👤 Author

**Jose Alvarez**  
Available for freelance Python scripting and automation work.  
📧 galdo0720@gmail.com
github.com/Galdo15
