#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, counts=None):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, params={'limit': 100}, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json().get('data', {})
        posts = data.get('children', [])
        
        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f'{word}: {count}')
            return
        else:
            titles = [post['data']['title'].lower() for post in posts]
            for title in titles:
                for word in word_list:
                    if word.lower() in title.split():
                        counts[word] = counts.get(word, 0) + 1
            after = data.get('after')
            return count_words(subreddit, word_list, counts) if after else counts
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
# count_words('python', ['python', 'java', 'javascript'])
