#!/usr/bin/python3

"""A script that queries the Reddit API
    and returns a count of all the users in it
"""
import requests


def number_of_subscribers(subreddit):
    """Counts the number of total subscribers in a subbreddit"""
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(URL, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    subscribers = results.get('subscribers')
    return subscribers
