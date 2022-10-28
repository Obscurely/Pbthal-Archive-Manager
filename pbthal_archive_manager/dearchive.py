import os


def extract():
    archives = []
    for archive in os.listdir("downloads"):
        archives.append(os.getcwd() + "/" + "downloads" + "/" + archive)

    os.chdir("music")

    for archive in archives:
        os.system(f'7z x "{archive}" -pb0nn13mCmurr@y')
