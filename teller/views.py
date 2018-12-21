from django.shortcuts import render
from django.http import JsonResponse
import requests
import config

def home(request):
    query = 'bitcoin'
    url = f'https://api.twitter.com/1.1/search/tweets.json?q={query}&lang=en'
    headers = {'authorization': f'Bearer {config.twitter_token}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    statuses = data['statuses']
    tweets = []
    for status_info in statuses:
        tweets.append(status_info['text'])

    return JsonResponse(tweets, safe=False)
