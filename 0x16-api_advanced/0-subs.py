#!/usr/bin/python3
"""
A module that returns the number of subscribers
"""

import requests


def get_subreddit_subscribers(subreddit):
    """Retrieves the number of subscribers in a given subreddit"""
    headers = {
        'User-Agent': ' '.join(['Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                                'AppleWebKit/537.36 (KHTML, like Gecko)',
                                'Chrome/58.0.3029.110 Safari/537.3'])}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
