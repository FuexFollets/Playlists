#! /bin/bash
#
yt-dlp -f ba -o "%(title)s" -x --audio-format flac --audio-quality 0 -P Favorites/ -a favorites.txt
