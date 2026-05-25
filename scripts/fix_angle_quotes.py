import glob
import re

for fpath in glob.glob("content/**/*.md", recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    new_content = re.sub(r'\(<"([^"]+)">\)', r'(\1)', content)
    new_content = re.sub(r"\(<'([^']+)'>\)", r"(\1)", new_content)

    if new_content != content:
        with open(fpath, "w") as f:
            f.write(new_content)
        print(f"Fixed: {fpath}")

print("Done")
