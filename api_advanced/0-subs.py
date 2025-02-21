#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return number of subscribers for a given subreddit
        and return 0 if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    head = requests.utils.default_head()
    head.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, head=head).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
