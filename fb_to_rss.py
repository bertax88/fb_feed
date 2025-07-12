from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

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

fg = FeedGenerator()
fg.title('Facebook Group Digest')
fg.link(href='https://www.facebook.com/groups/ssaexpats/')
fg.description('Manual Facebook group summary with comments')
fg.updated(datetime.now(timezone.utc))

for post in posts:
    if len(post) < 2:
        continue

    title = post[0]
    url = post[1]
    comments = '\n'.join(post[2:]) if len(post) > 2 else ''

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=url)
    fe.description(f"{comments}")
    fe.pubDate(datetime.now(timezone.utc))

output_path = '/storage/emulated/0/Documents/rss/facebook_feed.xml'
fg.rss_file(output_path)
print(f"✅ RSS feed with links and comments saved to: {output_path}")
