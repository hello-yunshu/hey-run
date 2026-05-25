#!/bin/bash
CDN_BASE="https://cdn.idleleo.com"
STATIC_DIR="/Users/yunshu/Documents/hugo/hey-run/static/images"
LIST_FILE="/tmp/wp_images_to_download.txt"

total=$(wc -l < "$LIST_FILE" | tr -d ' ')
count=0
success=0
failed=0

while IFS= read -r rel_path; do
    count=$((count + 1))
    dest="$STATIC_DIR/$rel_path"
    if [ -f "$dest" ]; then
        success=$((success + 1))
        continue
    fi
    mkdir -p "$(dirname "$dest")"
    url="$CDN_BASE/$rel_path"
    if curl -sfL -o "$dest" "$url" --max-time 30 --retry 2; then
        success=$((success + 1))
    else
        failed=$((failed + 1))
        echo "FAILED: $url"
        rm -f "$dest"
    fi
    if [ $((count % 50)) -eq 0 ]; then
        echo "Progress: $count/$total (success: $success, failed: $failed)"
    fi
done < "$LIST_FILE"

echo ""
echo "Download complete: $count/$total"
echo "Success: $success"
echo "Failed: $failed"
