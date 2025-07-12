import os

# Path to your Obsidian vault folder (change as needed)
obsidian_dir = '/storage/emulated/0/Documents/Obsidian/vault/FacebookPosts'

os.makedirs(obsidian_dir, exist_ok=True)

with open('fb_posts.txt', 'r') as f:
    lines = [line.rstrip() for line in f if line.strip()]

posts = []
current_post = []
for line in lines:
    if not line.startswith('>') and current_post:
        posts.append(current_post)
        current_post = [line]
    else:
        current_post.append(line)
if current_post:
    posts.append(current_post)

for i, post in enumerate(posts, 1):
    title = post[0].replace('/', '-')  # avoid slashes in filenames
    filename = f"{i:02d} - {title[:40]}.md"  # limit filename length
    filepath = os.path.join(obsidian_dir, filename)

    with open(filepath, 'w') as md_file:
        md_file.write(f"# {title}\n\n")
        for line in post[1:]:
            if line.startswith('>'):
                # Convert comment line to blockquote
                md_file.write(f"> {line[1:].strip()}\n\n")
            else:
                md_file.write(f"{line}\n\n")

print(f"✅ Markdown files saved to {obsidian_dir}")
