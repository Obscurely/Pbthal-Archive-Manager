import sys
import os
import search_pbthal
import real_debrid_download
import dearchive
import mass_rename
import album_covers
import album
import shutil
import recording_links


def search():
    # query = input("Album to search for: ")
    args = sys.argv
    args.reverse()
    args.pop()
    args.pop()
    args.reverse()

    query = ""
    for arg in args:
        query += arg + " "

    search_pbthal.search(query)


def download():
    links = []
    while True:
        current_input = input("Link to the album: ")
        if current_input == "":
            break

        links.append(current_input)

    for link in links:
        try:
            real_debrid_download.download(link)
        except:
            print(f"Couldn't download link '{link}', there was an error, moving on...")


def extract():
    dearchive.extract()


def rename():
    mass_rename.rename()


def covers():
    os.chdir("music")

    for folder in os.listdir():
        try:
            cover = album_covers.download_cover(folder)
        except:
            print(
                f"There was an error downloading a cover for the album {folder}, moving on..."
            )
            continue

        print(f"Downloading cover for {folder}...")

        with open(f"{folder}/folder.jpg", "wb") as f:
            f.write(cover)


def create_album():
    os.chdir("music")

    current_dir = os.getcwd()
    folders = os.listdir()

    for folder in folders:
        os.chdir(folder)
        album.create_album()
        os.chdir(current_dir)


def clean():
    shutil.rmtree("downloads")
    shutil.rmtree("music")

    os.mkdir("downloads")
    os.mkdir("music")


def links():
    recording_links.download_links()


def main():
    # create some needed folders
    os.mkdir("downloads")
    os.mkdir("music")

    args = sys.argv

    if len(args) == 1:
        print("Available options:")
        print(
            """
              s/search - grabs user input and searches for a literal match on pbthal website (offline) and possible download links on filefactory (offline), the filefactory links (the shared folders) are all available in the data folder, so you don't need to worry about anything (emailing etc.), just try and see!
              d/download - grabs user input (paste a link, hit enter, paste link, hit enter and so on. when done just hit enter with nothing typed in) and using your bearer (auth token for real debrid) that will be stored in .env (see github readme) will get the real debrid download link and download it to downloads.
              e/extract - extracts all the archives present in the downloads folder using pbthal's password and outputs them to music
              r/rename - mass renames all the folders present in the music folder by prefilling the input with the present name, allowing you to make any desired changes you want
              c/covers - gets album covers for all the folders present in the music folders (it uses the website vinyl-records.nl), it works well for my needs, but it may not have everything and will tell you when nothing was found. the searches are done using the folder's name.
              a/album - goes in everyfolder is the music folder and does the next steps: generate spectrograms for every song to check if it's a real flac or not, create a .m3u playlist, changes the tags (album, album artist, artist) and finally adds the cover to the song (cover has to be named folder.jpg)
              l/links - redownloads the recordings download links (from file factory), leaving it in here just in case anyone needs it.
              clean - deletes the folder downloads and music and recreats them, meaning you will lose anything you've downloaded and and extracted.
              """
        )
        exit()

    folders_structure = os.listdir()

    if "downloads" not in folders_structure:
        os.mkdir("downloads")
    elif "music" not in folders_structure:
        os.mkdir("music")

    arg = args[1]

    if arg == "s" or arg == "search":
        search()
    elif arg == "d" or arg == "download":
        download()
    elif arg == "e" or arg == "extract":
        extract()
    elif arg == "r" or arg == "rename":
        rename()
    elif arg == "c" or arg == "covers":
        covers()
    elif arg == "a" or arg == "album":
        create_album()
    elif arg == "l" or arg == "links":
        links()
    elif arg == "clean":
        clean()
    else:
        print(
            f"{arg} is an invalid argument, please run script without any args to see the help page!"
        )


if __name__ == "__main__":
    main()
