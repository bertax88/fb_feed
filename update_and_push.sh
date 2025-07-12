#!/data/data/com.termux/files/usr/bin/bash

# Step 1: Generate the RSS feed
python3 fb_to_rss.py

# Step 2: Export to Markdown for Obsidian
python3 fb_to_md.py

# Step 3: Stage all important files
git add facebook_feed.xml fb_posts.txt fb_to_rss.py fb_to_md.py update_and_push.sh

# Step 4: Commit with timestamp
git commit -m "Update feed & markdown export on $(date '+%Y-%m-%d %H:%M')" || echo "Nothing new to commit."

# Step 5: Push to GitHub
git push origin main
