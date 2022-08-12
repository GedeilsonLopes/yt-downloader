from unittest import result
from pytube import Playlist, YouTube
import ftransc
from os import path


def get_playlist(pl_url):

    playlist = Playlist(url=pl_url)
    return playlist


def get_information(music_url):
    yt = YouTube(url=music_url, use_oauth=False, allow_oauth_cache=True)
    return yt


def download_music(yt):
    stream = yt.streams.get_by_itag("140")
    stream.download("./music/")


def main():

    url = "https://youtu.be/9bZkp7q19f0"
    yt = get_information(url)
    download = download_music(yt)
    return download


main()
