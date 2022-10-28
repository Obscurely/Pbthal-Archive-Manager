import requests
import re
import os


def download_links():
    os.chdir("data")

    try:
        os.mkdir("recordings_links")
    except:
        pass

    for line in open("links").readlines():
        name = line.split(" ")[0]
        link = line.split(" ")[1]

        response_content = requests.get(f"{link}/?export=1").content
        recordings_links_macthes = re.findall(
            "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            bytes.decode(response_content),
        )

        recordings_links = []
        for link in recordings_links_macthes:
            recordings_links.append(link + "\n")

        with open(f"recordings_links/{name}", "w") as f:
            f.writelines(recordings_links)
