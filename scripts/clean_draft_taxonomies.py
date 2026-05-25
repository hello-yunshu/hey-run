import glob
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"

count = 0
for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    if "draft = true" not in content:
        continue

    if "categories" not in content and "tags" not in content:
        continue

    content = re.sub(r'^categories = \[.*\]\n?', '', content, flags=re.MULTILINE)
    content = re.sub(r'^tags = \[.*\]\n?', '', content, flags=re.MULTILINE)

    with open(fpath, "w") as f:
        f.write(content)
    count += 1

print(f"Removed categories/tags from {count} draft articles")
