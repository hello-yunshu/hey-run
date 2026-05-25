#!/usr/bin/env python3
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone, timedelta

import html2text

SQL_FILE = "/Users/yunshu/Documents/hugo/halo/halo_data/db_yunshu_halo_202604300330004sqpr.sql"
HUGO_CONTENT_DIR = "/Users/yunshu/Documents/hugo/hey-run/content"
HUGO_STATIC_DIR = "/Users/yunshu/Documents/hugo/hey-run/static"
HALO_UPLOAD_DIR = "/Users/yunshu/Documents/hugo/halo/halo2/attachments/upload"
CST = timezone(timedelta(hours=8))


def parse_sql_extensions(sql_file):
    records = []
    in_insert = False
    buf = ""

    with open(sql_file, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("INSERT INTO `extensions` VALUES"):
                in_insert = True
                buf = stripped
                if stripped.endswith(";"):
                    in_insert = False
                    records.extend(_parse_insert_values(buf))
                    buf = ""
            elif in_insert:
                buf += stripped
                if stripped.endswith(";"):
                    in_insert = False
                    records.extend(_parse_insert_values(buf))
                    buf = ""

    return records


def _read_sql_string(text, start):
    if start >= len(text) or text[start] != "'":
        return None, start
    i = start + 1
    chars = []
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            if i + 1 < len(text):
                nch = text[i + 1]
                if nch == "n":
                    chars.append("\n")
                elif nch == "t":
                    chars.append("\t")
                elif nch == "r":
                    chars.append("\r")
                elif nch == "\\":
                    chars.append("\\")
                elif nch == "'":
                    chars.append("'")
                elif nch == '"':
                    chars.append('"')
                elif nch == "0":
                    chars.append("\0")
                elif nch == "Z":
                    chars.append("\x1a")
                else:
                    chars.append("\\")
                    chars.append(nch)
                i += 2
            else:
                chars.append("\\")
                i += 1
        elif ch == "'":
            if i + 1 < len(text) and text[i + 1] == "'":
                chars.append("'")
                i += 2
            else:
                i += 1
                break
        else:
            chars.append(ch)
            i += 1
    return "".join(chars), i


def _parse_insert_values(insert_stmt):
    records = []
    content = insert_stmt
    idx = content.find("VALUES")
    if idx == -1:
        return records
    content = content[idx + 6 :].rstrip(";").strip()

    i = 0
    while i < len(content):
        if content[i] != "(":
            i += 1
            continue

        i += 1
        while i < len(content) and content[i] in (" ", "\t", "\n"):
            i += 1

        name, i = _read_sql_string(content, i)
        if name is None:
            continue

        while i < len(content) and content[i] in (",", " ", "\t", "\n"):
            i += 1

        if i < len(content) and content[i:].startswith("_binary"):
            i += len("_binary")
            while i < len(content) and content[i] == " ":
                i += 1

        data_str, i = _read_sql_string(content, i)

        while i < len(content) and content[i] in (",", " ", "\t", "\n"):
            i += 1

        version = None
        ver_start = i
        while i < len(content) and content[i] not in (")", ","):
            i += 1
        ver_str = content[ver_start:i].strip()
        if ver_str:
            try:
                version = int(ver_str)
            except ValueError:
                pass

        while i < len(content) and content[i] != ")":
            i += 1
        if i < len(content):
            i += 1
        while i < len(content) and content[i] in (",", " ", "\t", "\n"):
            i += 1

        if name and data_str:
            try:
                data = json.loads(data_str)
                records.append((name, data))
            except json.JSONDecodeError as e:
                print(f"JSON decode error for {name}: {e}", file=sys.stderr)
                records.append((name, None))

    return records


def clean_wp_blocks(html):
    html = re.sub(r"<!--\s*wp:[^>]*?-->", "", html)
    html = re.sub(r"<!--\s*/wp:[^>]*?-->", "", html)
    html = re.sub(r"<!--\s*wp:[^>]*?/\s*-->", "", html)
    return html.strip()


def html_to_markdown(html_content):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    h.unicode_snob = True
    h.protect_links = True
    h.wrap_links = False
    h.mark_code = True
    h.single_line_break = False

    cleaned = clean_wp_blocks(html_content)

    md = h.handle(cleaned)

    md = re.sub(r"```(\w+)\n\s*\n", r"```\1\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip() + "\n"

    return md


def process_image_urls(content):
    content = re.sub(
        r"(?:https?://cdn\.idleleo\.com)?(/wp-content/uploads/[^\s)\">]+)",
        lambda m: f"/images{m.group(1)}",
        content,
    )

    content = re.sub(r"/upload/([^\s)\"]+)", lambda m: f"/images/{m.group(1)}", content)

    return content


def format_datetime(dt_str):
    if not dt_str:
        return datetime.now(CST).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        dt = dt.astimezone(CST)
        return dt.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    except (ValueError, TypeError):
        return datetime.now(CST).strftime("%Y-%m-%dT%H:%M:%S+08:00")


def generate_front_matter(title, date_str, draft, description, tags, categories, slug=None, extra=None):
    lines = ["+++"]
    lines.append(f'title = {json.dumps(title, ensure_ascii=False)}')
    lines.append(f"date = {date_str}")
    lines.append(f"draft = {'true' if draft else 'false'}")
    if description:
        lines.append(f'description = {json.dumps(description, ensure_ascii=False)}')
    if slug:
        lines.append(f'slug = {json.dumps(slug, ensure_ascii=False)}')
    if tags:
        tag_strs = ", ".join(json.dumps(t, ensure_ascii=False) for t in tags)
        lines.append(f"tags = [{tag_strs}]")
    if categories:
        cat_strs = ", ".join(json.dumps(c, ensure_ascii=False) for c in categories)
        lines.append(f"categories = [{cat_strs}]")
    if extra:
        for k, v in extra.items():
            if isinstance(v, bool):
                lines.append(f"{k} = {'true' if v else 'false'}")
            elif isinstance(v, str):
                lines.append(f'{k} = {json.dumps(v, ensure_ascii=False)}')
            elif isinstance(v, int):
                lines.append(f"{k} = {v}")
    lines.append("+++")
    return "\n".join(lines)


def write_content_file(dir_path, front_matter, body):
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, "index.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n\n")
        f.write(body)
    return filepath


def slugify(text):
    if not text:
        return "untitled"
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = slug.strip("-")
    return slug if slug else "untitled"


def main():
    print("Parsing SQL backup...")
    records = parse_sql_extensions(SQL_FILE)
    print(f"Total records: {len(records)}")

    categories_map = {}
    tags_map = {}
    posts = {}
    snapshots = {}
    single_pages = {}
    attachments = {}

    for name, data in records:
        if not data:
            continue
        kind = data.get("kind", "")

        if name.startswith("/registry/content.halo.run/categories/"):
            cat_id = data.get("metadata", {}).get("name", "")
            cat_name = data.get("spec", {}).get("displayName", "")
            if cat_id and cat_name:
                categories_map[cat_id] = cat_name

        elif name.startswith("/registry/content.halo.run/tags/"):
            tag_id = data.get("metadata", {}).get("name", "")
            tag_name = data.get("spec", {}).get("displayName", "")
            if tag_id and tag_name:
                tags_map[tag_id] = tag_name

        elif kind == "Post":
            post_id = data.get("metadata", {}).get("name", "")
            if post_id:
                posts[post_id] = data

        elif kind == "Snapshot":
            snap_name = data.get("metadata", {}).get("name", "")
            if snap_name:
                snapshots[snap_name] = data

        elif kind == "SinglePage":
            page_id = data.get("metadata", {}).get("name", "")
            if page_id:
                single_pages[page_id] = data

        elif kind == "Attachment":
            att_id = data.get("metadata", {}).get("name", "")
            if att_id:
                attachments[att_id] = data

    print(f"Categories: {len(categories_map)}")
    print(f"Tags: {len(tags_map)}")
    print(f"Posts: {len(posts)}")
    print(f"Snapshots: {len(snapshots)}")
    print(f"SinglePages: {len(single_pages)}")
    print(f"Attachments: {len(attachments)}")

    posts_dir = os.path.join(HUGO_CONTENT_DIR, "posts")
    os.makedirs(posts_dir, exist_ok=True)

    migrated_posts = 0
    skipped_drafts = 0
    errors = []

    for post_id, post_data in posts.items():
        try:
            spec = post_data.get("spec", {})
            metadata = post_data.get("metadata", {})
            status = post_data.get("status", {})

            is_published = spec.get("publish", False)
            is_deleted = spec.get("deleted", False)

            if is_deleted:
                continue

            if not is_published:
                skipped_drafts += 1
                continue

            title = spec.get("title", "Untitled")
            slug = spec.get("slug", slugify(title))
            publish_time = spec.get("publishTime", "")
            excerpt = spec.get("excerpt", {}).get("raw", "") if spec.get("excerpt", {}) else ""
            if not excerpt:
                excerpt = status.get("excerpt", "")

            cat_ids = spec.get("categories", [])
            tag_ids = spec.get("tags", [])

            cat_names = [categories_map.get(c, c) for c in cat_ids if c]
            tag_names = [tags_map.get(t, t) for t in tag_ids if t]

            release_snapshot = spec.get("releaseSnapshot") or spec.get("headSnapshot")
            content_html = ""
            if release_snapshot and release_snapshot in snapshots:
                snap = snapshots[release_snapshot]
                snap_spec = snap.get("spec", {})
                raw_patch = snap_spec.get("rawPatch", "")
                content_patch = snap_spec.get("contentPatch", "")
                content_html = raw_patch or content_patch or ""

            if not content_html:
                head_snapshot = spec.get("headSnapshot")
                if head_snapshot and head_snapshot in snapshots:
                    snap = snapshots[head_snapshot]
                    snap_spec = snap.get("spec", {})
                    raw_patch = snap_spec.get("rawPatch", "")
                    content_patch = snap_spec.get("contentPatch", "")
                    content_html = raw_patch or content_patch or ""

            content_md = html_to_markdown(content_html) if content_html else ""
            content_md = process_image_urls(content_md)

            date_str = format_datetime(publish_time)

            front_matter = generate_front_matter(
                title=title,
                date_str=date_str,
                draft=False,
                description=excerpt,
                tags=tag_names,
                categories=cat_names,
                slug=slug,
            )

            safe_slug = re.sub(r'[<>:"/\\|?*]', "", slug).strip()
            if not safe_slug:
                safe_slug = slugify(title)
            post_dir = os.path.join(posts_dir, safe_slug)
            write_content_file(post_dir, front_matter, content_md)
            migrated_posts += 1

        except Exception as e:
            errors.append(f"Post {post_id}: {e}")
            print(f"Error processing post {post_id}: {e}", file=sys.stderr)

    print(f"\nMigrated posts: {migrated_posts}")
    print(f"Skipped drafts: {skipped_drafts}")

    pages_dir = HUGO_CONTENT_DIR
    os.makedirs(pages_dir, exist_ok=True)

    migrated_pages = 0
    for page_id, page_data in single_pages.items():
        try:
            spec = page_data.get("spec", {})
            metadata = page_data.get("metadata", {})

            is_deleted = spec.get("deleted", False)
            if is_deleted:
                continue

            title = spec.get("title", "Untitled")
            slug = spec.get("slug", slugify(title))

            release_snapshot = spec.get("releaseSnapshot") or spec.get("headSnapshot")
            content_html = ""
            if release_snapshot and release_snapshot in snapshots:
                snap = snapshots[release_snapshot]
                snap_spec = snap.get("spec", {})
                raw_patch = snap_spec.get("rawPatch", "")
                content_patch = snap_spec.get("contentPatch", "")
                content_html = raw_patch or content_patch or ""

            if not content_html:
                head_snapshot = spec.get("headSnapshot")
                if head_snapshot and head_snapshot in snapshots:
                    snap = snapshots[head_snapshot]
                    snap_spec = snap.get("spec", {})
                    raw_patch = snap_spec.get("rawPatch", "")
                    content_patch = snap_spec.get("contentPatch", "")
                    content_html = raw_patch or content_patch or ""

            content_md = html_to_markdown(content_html) if content_html else ""
            content_md = process_image_urls(content_md)

            publish_time = spec.get("publishTime", "") or metadata.get("creationTimestamp", "")
            date_str = format_datetime(publish_time)

            front_matter = generate_front_matter(
                title=title,
                date_str=date_str,
                draft=False,
                description="",
                tags=[],
                categories=[],
                slug=slug,
            )

            safe_slug = re.sub(r'[<>:"/\\|?*]', "", slug).strip()
            if not safe_slug:
                safe_slug = slugify(title)

            if safe_slug in ("about", "links", "contact"):
                page_dir = os.path.join(pages_dir, safe_slug)
            else:
                page_dir = os.path.join(pages_dir, safe_slug)

            write_content_file(page_dir, front_matter, content_md)
            migrated_pages += 1

        except Exception as e:
            errors.append(f"Page {page_id}: {e}")
            print(f"Error processing page {page_id}: {e}", file=sys.stderr)

    print(f"Migrated pages: {migrated_pages}")

    if os.path.isdir(HALO_UPLOAD_DIR):
        images_dir = os.path.join(HUGO_STATIC_DIR, "images")
        os.makedirs(images_dir, exist_ok=True)
        copied = 0
        for fname in os.listdir(HALO_UPLOAD_DIR):
            src = os.path.join(HALO_UPLOAD_DIR, fname)
            if os.path.isfile(src):
                dst = os.path.join(images_dir, fname)
                shutil.copy2(src, dst)
                copied += 1
        print(f"Copied {copied} media files to static/images/")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors[:20]:
            print(f"  {e}")

    print("\nMigration complete!")


if __name__ == "__main__":
    main()
