#!/usr/bin/python3
"""Queries the Reddit API and returns
the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns
       the number of subscribers"""

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    result = requests.get(url, headers=headers, allow_redirects=False)

    if result.status_code == 200:
        return (result.json().get("data").get("subscribers"))
    else:
        return 0
