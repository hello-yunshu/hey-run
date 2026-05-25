import glob
import os

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"

for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    fixed = content.replace('"+++', '"\n+++')
    fixed = fixed.replace('"\n+++\n', '"\n+++\n')

    if fixed != content:
        with open(fpath, "w") as f:
            f.write(fixed)

print("Done")
