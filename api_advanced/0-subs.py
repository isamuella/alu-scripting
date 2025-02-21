#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    If subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by ALU_student)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get('data', {}).get('subscribers', 0)

    except requests.exceptions.RequestException:
        return 0
