#!/usr/bin/python3
"""
Query Reddit API to get the top 10 hot post titles for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by ALU_student)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post["data"]["title"])
    else:
        print(None)
