# Vqd regex: (?<=vqd=')[0-9][-]\d+[-]\d+(?=')
import http.client
import re
import requests
import urllib.parse


def get_vqd(query: str):
    conn = http.client.HTTPSConnection("duckduckgo.com")
    payload = ""
    headers = {}
    conn.request(
        "GET",
        f"/?q={urllib.parse.quote(query)}+site%3Ahttps%3A%2F%2Fvinyl-records.nl%2F",
        payload,
        headers,
    )
    res = conn.getresponse()
    data = res.read()
    content = data.decode("utf-8")
    vqd = re.findall(r"(?<=vqd=')[0-9][-]\d+[-]\d+(?=')", content)[0]
    conn.close()
    return vqd


def get_album_cover_link(query: str):
    vqd = get_vqd(query)
    conn = http.client.HTTPSConnection("duckduckgo.com")
    payload = ""
    headers = {}
    conn.request(
        "GET",
        f"/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}%20site%3Ahttps%3A%2F%2Fvinyl%2Drecords.nl%2F&vqd={vqd}",
        payload,
        headers,
    )
    res = conn.getresponse()
    data = res.read()
    content = data.decode("utf-8")
    link = re.findall(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        content,
    )[1]
    conn.close()
    return link


def download_cover(album_query: str):
    album_cover_link = get_album_cover_link(album_query)
    album_cover = requests.get(album_cover_link).content

    return album_cover
