#!/usr/bin/python3
"""get the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """gets the titles of the first 10 hot posts"""

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    res = requests.get(url, headers={'User-Agent': 'TutTrue'},
                       allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
