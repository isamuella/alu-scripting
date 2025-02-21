#!/usr/bin/python3
"""
Module to query the Reddit API and print titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-script:v1.0 (by /u/your_username)"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
    
    if response.status_code == 404:
        print(None)
        return
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        results = response.json().get("data").get("children")
        for post in results:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
