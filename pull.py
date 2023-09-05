from __future__ import annotations

import requests
import subprocess
import os

from dataclasses import dataclass
from enum import Enum


class Source(Enum):
    YOUTUBE = 1
    OSU = 2


@dataclass
class Song:
    title: str
    source: Source
    url: str

    def download(self, path: str, replace: bool = False):
        exists: bool = os.path.exists(f"{path}/{self.title}.flac")

        if exists and not replace:
            return

        elif exists and replace:
            os.remove(f"{path}/{self.title}.flac")

        if self.source == Source.YOUTUBE:
            subprocess.run(
                [
                    "yt-dlp",
                    "-f",
                    "ba",
                    "-o",
                    f"{self.title}.flac",
                    "-x",
                    "--audio-format",
                    "flac",
                    "--audio-quality",
                    "0",
                    "-P",
                    path,
                    self.url,
                ]
            )
        elif self.source == Source.OSU:
            response: requests.Response = requests.get(
                self.url,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
                },
            )

            filename: str = f"{path}/{self.title}.flac"

            if not os.path.exists("ext"):
                os.mkdir("ext")

            open(f"ext/{self.title}.tar", "wb").write(response.content)
            subprocess.run(["unzip", f"ext/{self.title}.tar", "-d", "ext"])
            subprocess.run(["ffmpeg", "-i", "ext/audio.mp3", filename])
            subprocess.run(["rm", "-r", "ext"])


@dataclass
class Playlist:
    title: str
    directory_name: str
    songs: list[Song]

    def download(self, replace: bool = False):
        if not os.path.exists(self.directory_name):
            os.mkdir(self.directory_name)

        for song in self.songs:
            song.download(self.directory_name, replace)


songs = [
    Song(
        "Avenge Sevenfold - A little piece of heaven",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=qOWJ1-mEAXg",
    ),
    Song(
        "An feat - Amrita",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=3JyyroLwKEA",
    ),
    Song(
        "Creo - Sphere", Source.YOUTUBE, "https://www.youtube.com/watch?v=0ZUoFPLlVQU"
    ),
    Song(
        "Natalie Walker - Crush",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=OLTLjrF3QUg",
    ),
    Song(
        "Natalie Walker - Waking Dream",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=dVlvRTqEEB4",
    ),
    Song(
        "Crywolf - Eyes half closed",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=gD1ALm1l2zw",
    ),
    Song(
        "The Living Tombstone - This comes from the Inside",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=X6ELpluyZyg",
    ),
    Song(
        "The Living Tombstone - It's been so long",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=f2bV87F9zrM",
    ),
    Song(
        "Masahiro Godspeed Aoki - Frostbite",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=GW7jTcfbDd4",
    ),
    Song(
        "glass beach - Bedroom Community",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=1R4JcZbDvy8",
    ),
    Song(
        "alyankovic - Hardware Store",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=DFI6cV9slfI",
    ),
    Song(
        "Haatsune miku - Kotonoha Clinic",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=C7Dl3fMX23M",
    ),
    Song(
        "Polkadot Singray - Jet",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=phwvj0_XM4k",
    ),
    Song(
        "Jutes - Bad Dream ",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=m0X3p147Nxk",
    ),
    Song(
        "Undead Corporation - No Filter",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=E9tYFJJptE4",
    ),
    Song(
        "Trysail - Utsuroi",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=HnoP9ASPVXc",
    ),
    Song(
        "Fleur - Зов маяка",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=WKLr1r8opYA",
    ),
    Song(
        "Chanmina - Voice Memo No.5",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=0XnqcZx-0w4",
    ),
    Song(
        "Fujun Club - Travel & Ferry",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=8eEIMWopA5A",
    ),
    Song(
        "須田景凪 - 「veil」MV", Source.YOUTUBE, "https://www.youtube.com/watch?v=n7VZxg9pxkg"
    ),
    Song(
        "Innocent Key - Lunatic Red Eyes",
        Source.OSU,
        "https://assets.ppy.sh/artists/323/Touhou%20Tower%20Orchid/Innocent%20Key%20-%20Lunatic%20Red%20Eyes.osz",
    ),
    Song(
        "Maduk ft. Veela - Ghost Assassin",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=tEcggRukZCs",
    ),
    Song(
        "Nightwish - Escapist",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=eKuCFk1j_Io",
    ),
    Song(
        "S3RL feat. Tamika - Tell Me What You Want",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=G6uDfiVeJm4",
    ),
    Song(
        "DJ Fresh ft. Ellie Goulding - Flashlight (Radio Edit)",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=MVQXcDHvESM",
    ),
    Song(
        "Kikuohana - Nobore! Susume! Takai Tou",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=3Wlp-G-6M14",
    ),
    Song(
        "Trial & Error - Tokoyami no Keiyaku - SHOUJO",
        Source.OSU,
        "https://assets.ppy.sh/artists/20/Songs/Trial%20%26%20Error%20-%20Tokoyami%20no%20Keiyaku%20KEGARETA-SHOUJO%20feat.%20GUMI.osz",
    ),
    Song(
        "Kinoko Teikoku - Whirlpool",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=33JNwxSNNNY",
    ),
    Song(
        "Serebro - I Won't Give You Up",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=HEsX1FeZ25Y",
    ),
    Song(
        "T.a.t.u. - All The Things She Said",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=ujpvNvSgcic",
    ),
    Song(
        "Aiobahn & Yunomi - Ginga Tetsudou no Penguin",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=8oUnO8H6x1s",
    ),
    Song(
        "Cartoon - Whatever I do (feat. Kostja)",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=6CbaTLNBTjM",
    ),
    Song(
        "S3RL - Well, That Was Awkward",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=xnDeddWiUaw",
    ),
    Song(
        "Dustcell - Dero",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=iFKXsCZGV8A",
    ),
    Song(
        "Yooh - Ice Angel",
        Source.OSU,
        "https://assets.ppy.sh/artists/218/Yoohsics%20-REVIVAL-/Yooh%20-%20Ice%20Angel.osz",
    ),
    Song(
        "Ice Nine Kills - Merry Axe-Mas",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=P6bivDelhWc",
    ),
    Song(
        "Dreamcatcher - You And I",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=I5_BQAtwHws",
    ),
    Song(
        "Katarzyna Bogusz, Ola Maciejewska, Przemyslaw Kleczkowski - Blogoslawieni Milosierni",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=ETrhmFC_1TA",
    ),
    Song(
        "Sarah Connor - Cold As Ice Remix",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=E3yGF9PFetQ",
    ),
    Song(
        "Wanima - Gong",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=nJceYEtgBsc",
    ),
    Song(
        "Epica - Victims of Contingency",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=i7IIYIFljZM",
    ),
    Song(
        "Waterflame - Thunderzone v2",
        Source.YOUTUBE,
        "https://www.youtube.com/watch?v=oIu1o536GmI",
    ),
]

playlist = Playlist("Favorites", "Favorites", songs)


def main():
    playlist.download()


if __name__ == "__main__":
    main()
