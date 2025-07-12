from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Read all posts from file
with open('fb_posts.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

# Group lines into posts
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

# Create RSS feed
fg = FeedGenerator()
fg.title('Facebook Group Digest')
fg.link(href='http://localhost/fb')
fg.description('Manually curated Facebook group posts + comments')
fg.updated(datetime.now(timezone.utc))  # Ensures feed updates every time

# Add each entry
for post in posts:
    title = post[0]
    body = '\n'.join(post[1:]) if len(post) > 1 else ''
    fe = fg.add_entry()
    fe.title(title)
    fe.description(body)
    fe.pubDate(datetime.now(timezone.utc))  # Avoid timezone error

# Save the feed
output_path = '/storage/emulated/0/Documents/rss/facebook_feed.xml'
fg.rss_file(output_path)
print(f"✅ RSS feed with full text saved to: {output_path}")
