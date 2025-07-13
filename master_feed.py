import feedparser
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

output_path = '/storage/emulated/0/Documents/rss/master_feed.xml'
facebook_feed = '/storage/emulated/0/Documents/rss/facebook_feed.xml'
sources = [
    facebook_feed,
    'https://www.reddit.com/r/ssa/.rss',
    'https://blog.ssa.gov/feed/'
]

fg = FeedGenerator()
fg.title('Unified SSA + Facebook Feed')
fg.link(href='https://ssa.gov')
fg.description('Combined updates from Facebook, Reddit, and SSA blog')
fg.language('en')
fg.updated(datetime.now(timezone.utc))

for src in sources:
    print(f"Parsing: {src}")
    feed = feedparser.parse(src)
    for entry in feed.entries:
        fe = fg.add_entry()
        fe.title(entry.get('title', 'No title'))
        fe.link(href=entry.link)
        fe.description(entry.get('summary', ''))
        fe.pubDate(datetime.now(timezone.utc))

fg.rss_file(output_path)
print(f"✅ Combined RSS feed saved to: {output_path}")
