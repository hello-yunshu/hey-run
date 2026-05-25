import re
import glob

for fpath in glob.glob("content/**/*.md", recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    content = re.sub(r'\]\((/images/[^)"]+)"\)', r'](\1)', content)
    content = re.sub(r'!\["([^"]+)"\]', r'![\1]', content)

    with open(fpath, "w") as f:
        f.write(content)

print("Fixed image references")
