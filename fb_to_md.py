import os

obsidian_dir = '/storage/emulated/0/Documents/Obsidian/vault/FacebookPosts'
os.makedirs(obsidian_dir, exist_ok=True)

with open('fb_posts.txt', 'r') as f:
    lines = [line.rstrip() for line in f if line.strip()]

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

for i, post in enumerate(posts, 1):
    if len(post) < 2:
        continue  # Skip incomplete posts

    title = post[0].replace('/', '-')
    url = post[1]
    comments = post[2:] if len(post) > 2 else []

    filename = f"{i:02d} - {title[:40]}.md"
    filepath = os.path.join(obsidian_dir, filename)

    with open(filepath, 'w') as md:
        md.write(f"# {title}\n\n")
        md.write(f"[View on Facebook]({url})\n\n")
        for line in comments:
            if line.startswith('>'):
                md.write(f"> {line[1:].strip()}\n\n")
            else:
                md.write(f"{line}\n\n")

print(f"✅ Markdown posts with links saved to {obsidian_dir}")
