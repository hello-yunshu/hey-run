import glob
import hashlib
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"
SVG_OPTIONS = [
    "/img/fireflies.svg",
    "/img/lavalamp.svg",
    "/img/rain.svg",
    "/img/ripples.svg",
    "/img/traffic.svg",
    "/img/waves.svg",
]


def extract_first_image(content):
    md_match = re.search(r"!\[[^\]]*\]\(([^)]+)\)", content)
    if md_match:
        url = md_match.group(1)
        if url.startswith("/images/") or url.startswith("http"):
            return url

    html_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    if html_match:
        url = html_match.group(1)
        if url.startswith("/images/") or url.startswith("http"):
            return url

    return None


def get_svg_for_slug(slug):
    h = hashlib.md5(slug.encode()).hexdigest()
    idx = int(h, 16) % len(SVG_OPTIONS)
    return SVG_OPTIONS[idx]


def process_file(fpath):
    with open(fpath, "r") as f:
        content = f.read()

    if "featureimage" in content:
        return False

    plus_end = content.find("+++")
    if plus_end == -1:
        return False
    plus_end2 = content.find("+++", plus_end + 3)
    if plus_end2 == -1:
        return False

    front_matter = content[plus_end + 3 : plus_end2]
    body = content[plus_end2 + 3 :]

    slug_match = re.search(r'slug\s*=\s*"([^"]*)"', front_matter)
    slug = slug_match.group(1) if slug_match else os.path.basename(os.path.dirname(fpath))

    first_img = extract_first_image(body)

    if first_img:
        feature = first_img
    else:
        feature = get_svg_for_slug(slug)

    new_front = front_matter.rstrip() + f'\nfeatureimage = "{feature}"'
    new_content = "+++" + new_front + "+++" + body

    with open(fpath, "w") as f:
        f.write(new_content)

    return True


count = 0
for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    if process_file(fpath):
        count += 1

print(f"Added featureimage to {count} files")
