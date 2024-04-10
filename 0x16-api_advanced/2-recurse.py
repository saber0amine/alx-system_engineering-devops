#!/usr/bin/python3
""" 2-recurse.py module """
from requests import get


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns  list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) \
                Gecko/20100101 Firefox/108.0"
    }
    params = {
            "limit": 100,
            "count": count,
            "after": after
    }
    response = get(url, params=params, headers=headers,
                   allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for child in res.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
