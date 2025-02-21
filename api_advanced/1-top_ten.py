#!/usr/bin/python3
"""
Query Reddit API for the titles of the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    Prints None if the subreddit is invalid or no posts are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0 (by ALU_student)"}
    params = {"limit": 10}  # Get only the first 10 posts

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        # If subreddit doesn't exist or request fails (not 200 OK), print None
        if response.status_code != 200:
            print(None)
            return

        # Try parsing JSON
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # If no posts are found, print None
        if not posts:
            print(None)
            return

        # Print the top 10 post titles
        for post in posts:
            print(post['data']['title'])

    except requests.RequestException:
        # If network issues or invalid responses, print None
        print(None)

