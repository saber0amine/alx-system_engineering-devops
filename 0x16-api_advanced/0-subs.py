#!/usr/bin/python3
""" function that executes an api get request """
from requests import get


def number_of_subscribers(subreddit):
    """ api request to get number of subscribers """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    lien = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    response = get(lien, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers', 0)
    return subscribers
