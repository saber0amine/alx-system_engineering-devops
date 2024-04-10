#!/usr/bin/python3
"""number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subscribers for a given subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers={'User-Agent': 'TutTrue'}).json()
    return res.get('data', {}).get('subscribers', 0)
