import requests
from requests import Request, Session
import re
import urllib.parse
from dotenv import load_dotenv
import os


def download(link: str):
    load_dotenv()

    bearer = os.getenv("bearer")

    data = {
        "link": link,
    }

    headers = {"authorization": bearer}

    request = Request(
        "POST",
        "https://app.real-debrid.com/rest/1.0/unrestrict/link",
        headers=headers,
        files={
            "link": (None, data["link"]),
        },
    ).prepare()

    s = Session()
    response = s.send(request)

    download_link = str(
        re.findall('(?<="download": ")https:.+(?=",\n)', response.text)[0]
    ).replace("\\", "")
    print("Downloading " + download_link)

    file = requests.get(download_link).content

    with open("downloads/" + urllib.parse.unquote(link.split("/")[-1]), "wb") as f:
        f.write(file)
