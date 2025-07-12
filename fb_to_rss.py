from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Load posts from the file
with open('fb_posts.txt', 'r') as f:
    posts = [line.strip() for line in f if line.strip()]

fg = FeedGenerator()
fg.title('Facebook Group Feed')
fg.link(href='http://localhost/facebook')
fg.description('Offline Facebook group digest with full text')

for post in posts:
    # Try to make a meaningful title
    title = post.split('.')[0][:60]  # first sentence or 60 chars
    if len(title) < 10:
        title = post[:60]  # fallback

    entry = fg.add_entry()
    entry.title(title.strip())
    entry.description(post.strip())
    entry.pubDate(datetime.now(timezone.utc))

# Save the RSS feed to shared storage
output_path = '/storage/emulated/0/Documents/rss/facebook_feed.xml'
fg.rss_file(output_path)
print(f"✅ RSS feed with full text saved to: {output_path}")
