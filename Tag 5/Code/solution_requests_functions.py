#!/usr/bin/env python3
# coding: utf8

import requests

def download_web_page():
    url = input("url:")
    if len(url) < 4:
        url = 'https://moodle.bztf.ch/course/view.php?id=2405'

    resp = requests.get(url)
    print(f"URL: {url}")
    print(resp.text)