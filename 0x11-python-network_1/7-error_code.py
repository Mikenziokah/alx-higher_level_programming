#!/usr/bin/python3
"""
script that takes in a URL, sends a request to
the URL and displays the body of the response
"""
import sys
import requests


if __name__ == '__main__':
    page = requests.get(sys.argv[1])

    if page.status_code >= 400:
        print("Error code: {}".format(page.status_code))
    else:
        print(page.text)
