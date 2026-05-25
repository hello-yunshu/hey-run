import glob
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"

count = 0
for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    new_content = re.sub(r'"\]},\s*"type":\s*"CHANGE"\}\]', '', content)

    if new_content != content:
        with open(fpath, "w") as f:
            f.write(new_content)
        count += 1

print(f"Cleaned from {count} files")
