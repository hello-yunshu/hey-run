import glob
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"
CDN_BASE = "https://cdn.idleleo.com"

for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    new_content = re.sub(
        r'featureimage = "/images/wp-content/',
        f'featureimage = "{CDN_BASE}/wp-content/',
        content,
    )

    if new_content != content:
        with open(fpath, "w") as f:
            f.write(new_content)

print("Done")
