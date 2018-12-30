from django.shortcuts import render
from django.http import JsonResponse
from watson_developer_cloud import ToneAnalyzerV3
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
    text = ' '.join(tweets)

    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='Si1t19DXhzGFq3wgS2rSwvyncuQ6fzX8jwdoe28qWW1s',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    # text = 'I am so in love with the Watson API, although it was a long and arduous process getting this thing established. I wish the documentation was more nuanced, especially in regards to junior developers. Its frustrating slogging through unhelpful docs.'

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    return JsonResponse(text, safe=False)




    #
    # return JsonResponse(tweets, safe=False)
