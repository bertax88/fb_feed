#!/data/data/com.termux/files/usr/bin/bash

python3 fb_to_rss.py
python3 fb_to_md.py

git add facebook_feed.xml fb_posts.txt fb_to_rss.py fb_to_md.py update_and_push.sh
git commit -m "Update RSS & Markdown on $(date '+%Y-%m-%d %H:%M')" || echo "Nothing new to commit."
git push origin main
