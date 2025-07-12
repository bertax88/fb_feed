#!/data/data/com.termux/files/usr/bin/bash

# Generate updated RSS feed
python3 fb_to_rss.py

# Stage the RSS file
git add facebook_feed.xml

# Commit with timestamp
git commit -m "Update RSS feed on $(date '+%Y-%m-%d %H:%M')"

# Push to GitHub
git push origin main
