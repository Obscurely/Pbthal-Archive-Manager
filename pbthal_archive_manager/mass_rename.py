import gnureadline as readline
import os


def rlinput(prompt, prefill=""):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)  # or raw_input in Python 2
    finally:
        readline.set_startup_hook()


def rename():
    os.chdir("music")

    for file in os.listdir():
        name = rlinput("Folder: ", file)
        os.rename(file, name)
