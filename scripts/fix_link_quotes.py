import glob
import re

for fpath in glob.glob("content/**/*.md", recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    if '](\\"' not in content and "]('" not in content:
        continue

    has_quotes = False
    for m in re.finditer(r'\]\(\\?"(https?://[^"]+)"\\?\)', content):
        has_quotes = True
        break

    if not has_quotes:
        for m in re.finditer(r"\]\(\\?'(https?://[^']+)\\?'\)", content):
            has_quotes = True
            break

    if not has_quotes:
        continue

    print(f"Fixing: {fpath}")

    content = re.sub(r'\]\(\\?"(https?://[^"]+)"\\?\)', r'](\1)', content)
    content = re.sub(r"\]\(\\?'(https?://[^']+)'\\?\)", r"](\1)", content)

    with open(fpath, "w") as f:
        f.write(content)

print("Done")
