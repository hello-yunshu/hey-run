import glob
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"
CUTOFF = "2024-01-01"

count = 0
for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    date_match = re.search(r'date\s*=\s"?(\d{4}-\d{2}-\d{2})', content)
    if not date_match:
        continue

    date_str = date_match.group(1)
    if date_str < CUTOFF:
        content = content.replace("draft = false", "draft = true", 1)
        with open(fpath, "w") as f:
            f.write(content)
        count += 1

print(f"Set draft=true for {count} articles before {CUTOFF}")
