import glob
import os
import re

CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"

ARTICLE_META = {
    "use-reality": {
        "categories": ["网络技术"],
        "tags": ["Xray", "Reality", "代理", "CDN"],
    },
    "bushu-reality-balance": {
        "categories": ["网络技术"],
        "tags": ["Xray", "Reality", "负载均衡", "代理"],
    },
    "da-jian-xray-reality-xie-yi-fu-wu-qi": {
        "categories": ["网络技术"],
        "tags": ["Xray", "Reality", "服务器搭建", "代理"],
    },
    "1715234393850": {
        "categories": ["网络技术"],
        "tags": ["Xray", "负载均衡", "脚本", "代理"],
    },
    "reality-xie-yi-de-feng-xian": {
        "categories": ["网络技术"],
        "tags": ["Xray", "Reality", "安全", "代理"],
    },
}

count = 0
for fpath in glob.glob(os.path.join(CONTENT_DIR, "**/index.md"), recursive=True):
    with open(fpath, "r") as f:
        content = f.read()

    if "draft = true" in content:
        continue

    slug_match = re.search(r'slug\s*=\s"([^"]*)"', content)
    if not slug_match:
        continue
    slug = slug_match.group(1)

    if slug not in ARTICLE_META:
        continue

    meta = ARTICLE_META[slug]

    if "categories" in content or "tags" in content:
        continue

    plus_end = content.find("+++")
    plus_end2 = content.find("+++", plus_end + 3)
    if plus_end2 == -1:
        continue

    front_matter = content[plus_end + 3 : plus_end2]
    body = content[plus_end2 + 3 :]

    cat_str = ", ".join(f'"{c}"' for c in meta["categories"])
    tag_str = ", ".join(f'"{t}"' for t in meta["tags"])

    new_front = front_matter.rstrip()
    new_front += f'\ncategories = [{cat_str}]'
    new_front += f'\ntags = [{tag_str}]'

    new_content = "+++" + new_front + "\n+++" + body

    with open(fpath, "w") as f:
        f.write(new_content)
    count += 1

print(f"Added categories/tags to {count} articles")
