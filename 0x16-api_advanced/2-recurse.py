#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, params={'limit': 100}, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json().get('data', {})
        posts = data.get('children', [])
        
        if not posts:
            return hot_list
        else:
            titles = [post['data']['title'] for post in posts]
            hot_list.extend(titles)
            after = data.get('after')
            return recurse(subreddit, hot_list) if after else hot_list
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
# print(recurse('python'))
