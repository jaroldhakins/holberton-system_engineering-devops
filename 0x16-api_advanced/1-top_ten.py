#!/usr/bin/python3
"""prints the titles of the first 10 hot
    posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot
    posts listed for a given subreddit"""
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    p = {'limit': 10}
    result = requests.get(url, headers=headers, p=p, allow_redirects=False)
    if result.status_code == 200:
        titles_ = result.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
