#!/data/data/com.termux/files/usr/bin/bash

# Step 1: Generate the feed
python3 fb_to_rss.py

# Step 2: Stage all updated files
git add facebook_feed.xml fb_posts.txt fb_to_rss.py update_and_push.sh

# Step 3: Commit with timestamp
git commit -m "Update feed on $(date '+%Y-%m-%d %H:%M')" || echo "Nothing new to commit."

# Step 4: Push to GitHub
git push origin main
