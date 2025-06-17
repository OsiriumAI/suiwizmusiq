# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from yt_dlp import YoutubeDL

# Extracted LOGIN_INFO cookie value from cookies.txt (line 7)
LOGIN_INFO_VALUE = "AFmmF2swRQIgKLbSgkWPvNybp6wZubGNic63yz5HpTvd4HJAOBXNrFICIQC_HzGbolvM6DaXnw21NF6onp15h2AaSQm4EeKXTxiA5w:QUQ3MjNmeXBMZHRUZDBTUEdrTWh0RjVCTHBRVUhUWng4a3Zvb1ZXZnhWalVTYmZxMXZqVEZGbW8zNjQtRG5yQVhfWDlyRzVqekFKT0tHMnB1dnptZFBZZmRTU1JPNkRFcnlvbkM3ZkRmaTRSQkF4MUpjbk95ZVlNLUZZakVhb0Fvd1VUX0p0X2VGWmtITGFCckZSaENMRmZ1YUNqb0liN0FR"

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "cookies": {
        ".youtube.com": {"LOGIN_INFO": LOGIN_INFO_VALUE}
    },
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}
ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    sin = ydl.extract_info(url, False)
    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    ydl.download([url])
    return x_file
