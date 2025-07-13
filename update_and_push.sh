#!/data/data/com.termux/files/usr/bin/bash

# Navigate to repo
cd ~/fb_feed || exit

# Run Facebook posts to RSS
python3 fb_to_rss.py

# Run Facebook posts to Markdown with groups and tagging
python3 fb_to_md.py

# Generate master combined RSS feed
python3 master_feed.py

# Git add and commit changes
git add .

commit_message="Update feed on $(date '+%Y-%m-%d %H:%M')"
git commit -m "$commit_message"

# Push changes using saved token authentication (ensure .netrc or SSH key setup)
git push origin main
