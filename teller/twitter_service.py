import os
import requests
from django.http import JsonResponse


def retrieve_twitter_data(query):
    url = f'https://api.twitter.com/1.1/search/tweets.json?q={query}&lang=en&count=100'
    headers = {'authorization': f'Bearer {os.environ.get("twitter_token")}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['statuses']
