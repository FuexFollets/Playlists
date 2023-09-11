# Playlists
Some of my music

# How to use

To create your own identical repo of songs, copy `pull.py` and `push.py` (their importance will be noted later)

## Adding songs
The `playlist` object in `pull.py` can be used to create playlist. It is constructed with a list of `Song` objects. `Song` objects require a title, source, and link. Additional sources can be implemented.

### Push.py

This script serves the purpose of pushing sound files to the repo. This adds each song individually so that the git transfer socket does not close while more data needs to be uploaded. Therefore, it must be added in segments. This also does not require the use of git-lfs which is limited to 2gb per user unless more space is paid for.
