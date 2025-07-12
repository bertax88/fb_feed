from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Read and parse
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

# Set up feed
fg = FeedGenerator()
fg.title('Facebook Group Digest')
fg.link(href='http://localhost/fb')
fg.description('Curated Facebook group posts + comments')
fg.updated(datetime.now(timezone.utc))

# Add entries
for post in posts:
    if len(post) < 2:
        continue  # skip incomplete blocks

    title = post[0]
    url = post[1]
    comments = '\n'.join(post[2:]) if len(post) > 2 else ''

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=url)
    fe.description(comments)
    fe.pubDate(datetime.now(timezone.utc))

# Save RSS file
output_path = '/storage/emulated/0/Documents/rss/facebook_feed.xml'
fg.rss_file(output_path)
print(f"✅ RSS feed with links saved to: {output_path}")
