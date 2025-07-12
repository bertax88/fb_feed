import os
import re
from datetime import datetime

# === CONFIG ===
obsidian_dir = '/storage/emulated/0/Documents/Obsidian/vault/FacebookPosts'
default_tags = ['#facebook', '#ssa']
os.makedirs(obsidian_dir, exist_ok=True)

# === LOAD POSTS ===
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

# === EXPORT EACH POST ===
for i, post in enumerate(posts, 1):
    if len(post) < 2:
        continue

    title = post[0]
    url = post[1]
    comments = post[2:] if len(post) > 2 else []

    # === Safe filename
    safe_title = re.sub(r'[<>:"/\\|?*]', '-', title)
    safe_title = re.sub(r'\s+', ' ', safe_title).strip()
    filename = f"{i:02d} - {safe_title[:40]}.md"
    filepath = os.path.join(obsidian_dir, filename)

    # === Write Markdown file
    with open(filepath, 'w') as md:
        md.write(f"---\n")
        md.write(f"title: \"{title}\"\n")
        md.write(f"source: \"{url}\"\n")
        md.write(f"date: {datetime.now().strftime('%Y-%m-%d')}\n")
        md.write(f"tags: {default_tags}\n")
        md.write(f"---\n\n")

        md.write(f"# {title}\n\n")
        md.write(f"[📌 View original post on Facebook]({url})\n\n")

        for line in comments:
            if line.startswith('>'):
                md.write(f"> {line[1:].strip()}\n\n")
            else:
                md.write(f"{line}\n\n")

print(f"✅ Markdown with frontmatter + tags saved to: {obsidian_dir}")
