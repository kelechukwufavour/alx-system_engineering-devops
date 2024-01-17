#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0
