#!/usr/bin/python3
"""
Module to query the Reddit API and print titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query
        
    Returns:
        None
    """
    headers = {'User-Agent': 'python:alu-script:v1.0 (by /u/your_username)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        print(post.get('data', {}).get('title'))
