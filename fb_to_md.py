import os
import re
from datetime import datetime

# === Config ===
group_map = {
    '604353278592635': ('SSA', '#ssa'),
    'WEPGPO': ('WEPGPO', '#wepgpo'),
    '1511876379136842': ('Vietnam', '#vietnam'),
    'share/p/19ZpTiN6Aj': ('Shared', '#shared')
}

default_tags = ['#facebook']

# Load and parse posts
with open('fb_posts.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

posts = []
current = []
for line in lines:
    if not line.startswith('>') and current:
        posts.append(current)
        current = [line]
    else:
        current.append(line)
if current:
    posts.append(current)

def detect_group_tag(url):
    for key, (folder, tag) in group_map.items():
        if key in url:
            return folder, tag
    return 'Misc', '#misc'

year = datetime.now().strftime('%Y')

for i, post in enumerate(posts, 1):
    if len(post) < 2:
        continue

    title = post[0]
    url = post[1]
    comments = post[2:] if len(post) > 2 else []

    folder, tag = detect_group_tag(url)
    base_dir = f'/storage/emulated/0/Documents/Obsidian/vault/FacebookPosts/{folder}/{year}'
    os.makedirs(base_dir, exist_ok=True)

    safe_title = re.sub(r'[<>:"/\\|?*]', '-', title)
    safe_title = re.sub(r'\s+', ' ', safe_title).strip()
    filename = f"{i:02d} - {safe_title[:40]}.md"
    filepath = os.path.join(base_dir, filename)

    tags = default_tags + [tag]

    with open(filepath, 'w') as md:
        md.write(f"---\n")
        md.write(f"title: \"{title}\"\n")
        md.write(f"source: \"{url}\"\n")
        md.write(f"date: {datetime.now().strftime('%Y-%m-%d')}\n")
        md.write(f"tags: {tags}\n")
        md.write(f"---\n\n")

        md.write(f"# {title}\n\n")
        md.write(f"[📌 View original post on Facebook]({url})\n\n")

        for line in comments:
            if line.startswith('>'):
                md.write(f"> {line[1:].strip()}\n\n")
            else:
                md.write(f"{line}\n\n")

print(f"✅ Markdown notes saved and organised by group and year.")
