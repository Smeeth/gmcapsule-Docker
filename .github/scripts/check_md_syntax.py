import sys
from pathlib import Path

error_found = False

for file in Path("docs/source").rglob("*.md"):
    content = file.read_text(encoding="utf-8")

    # Prüfe auf ungerade Anzahl von Code-Fences
    if content.count("```") % 2 != 0:
        print(f"❌ ERROR: Unmatched code fences in {file}")
        error_found = True
    else:
        print(f"✅ {file} OK")

if error_found:
    sys.exit(1)
