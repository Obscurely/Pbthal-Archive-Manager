# Vqd regex: (?<=vqd=')[0-9][-]\d+[-]\d+(?=')
# qwant regex (?<="media":")https:\\u002F\\u002Fvinyl-records.nl\\u002F\w+\\u002Fphoto-gallery\\u002F[\w|-]*\\u002F[\w|-]*\\u002F[\w|-]*.jpg(?=")
import http.client
import re
import requests
import urllib.parse


def get_album_cover_link(query: str):
    # conn = http.client.HTTPSConnection("duckduckgo.com")
    # payload = ""
    # headers = {}
    # conn.request(
    #     "GET",
    #     f"/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}%20site%3Ahttps%3A%2F%2Fvinyl%2Drecords.nl%2F&vqd={vqd}",
    #     payload,
    #     headers,
    # )
    # res = conn.getresponse()
    # data = res.read()
    # content = data.decode("utf-8")
    url = f"https://www.qwant.com/?q={urllib.parse.quote(query)}%20site%3Ahttps%3A%2F%2Fvinyl-records.nl&t=images"
    headers = {
        "Host": "www.qwant.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Connection": "keep-alive",
        "User-Agent": "PostmanRuntime/7.29.2",
    }
    content = bytes.decode(requests.get(url, headers=headers).content)
    link = re.findall(
        # "(?<=\"media\":\")https:\\\\u002F\\\\u002Fvinyl-records.nl\\\\u002F\\w+\\\\u002Fphoto-gallery\\u002F[\\w|-]*\\\\u002F[\\w|-]*\\\\u002F[\\w|-]*.jpg(?=\")",
        r"(?<=\"media\":\")https:\\u002F\\u002Fvinyl-records.nl\\u002F\w+\\u002Fphoto-gallery\\u002F[\w|-]*\\u002F[\w|-]*\\u002F[\w|-]*.jpg(?=\")",
        content,
    )[0]
    return str(link).replace("\\u002F", "/")


def download_cover(album_query: str):
    album_cover_link = get_album_cover_link(album_query)
    album_cover = requests.get(album_cover_link).content

    return album_cover
