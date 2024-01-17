#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        if response.status_code == 404:
            print("None")
            return

        results = response.json().get("data")
        if not results or "children" not in results:
            print("None")
            return

        [print(c.get("data").get("title")) for c in results.get("children")]

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        print("None")

# Example usage:
# top_ten('python')
