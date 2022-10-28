import music_tag
import os
import shutil
import math


def create_spectrogram(file: str, out: str):
    out_file = file + ".png"
    os.system(f'sox "{file}" -n spectrogram -o "{out_file}"')
    shutil.move(out_file, out + "/" + out_file)


def change_tags(file: str, artist: str, album: str):
    # Load flac
    f = music_tag.load_file(file)

    # Set the basics
    f["artist"] = artist
    f["albumartist"] = artist
    f["album"] = album

    # Set Artwork
    with open("folder.jpg", "rb") as img_in:
        f["artwork"] = img_in.read()

    # Save
    f.save()


def append_to_playlist(flac, root_folder: str):
    f = music_tag.load_file(flac)
    flac_length = math.floor(float(str(f["#length"])))
    track_title = f["tracktitle"]
    track_artist = f["artist"]
    playlist = open(root_folder + ".m3u", "a")
    playlist.write(f"#EXTINF:{flac_length},{track_artist} - {track_title}\n{flac}\n")


def create_album():
    root_folder = os.getcwd().split("/")[-1]
    artist = root_folder.split(" - ")[0]
    album = root_folder.split(" - ")[1]

    files = os.listdir()
    flacs = []

    for file in files:
        if file.split(".")[-1] == "flac":
            flacs.append(file)

    if "Spectrograms" not in os.listdir():
        os.mkdir("Spectrograms")
        for flac in flacs:
            create_spectrogram(flac, "Spectrograms")

    for flac in flacs:
        change_tags(flac, artist, album)

    playlist = open(root_folder + ".m3u", "w")
    playlist.write("#EXTM3U\n")
    playlist.close()

    for flac in flacs:
        append_to_playlist(flac, root_folder)
