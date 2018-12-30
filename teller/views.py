from django.shortcuts import render
from django.http import JsonResponse
from watson_developer_cloud import ToneAnalyzerV3
import re
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

    cleaned_tweets = []
    for tweet in tweets:
    # CLEAN TWEET CONTRACTIONS
        contractions = {"'s":"is", "'re":"are", "'ve":"have", "'nt":"not", "'d":"would", "'m":"am", "'ll":"will"}
        poss_contractions = tweet.replace("'", " '").split(" ")
        for poss_contraction in poss_contractions:
            non_contraction = [contractions[poss_contraction] if poss_contraction in contractions else poss_contraction for poss_contraction in poss_contractions]

            # CLEAN @TWITTERHANDLE & URLS
            sentance = " ".join([word for word in non_contraction if 'http' not in word and '@' not in word])
            # CLEAN HASHTAGS
            tweet = sentance.replace("#", "")

        cleaned_tweets.append(tweet)

    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='Si1t19DXhzGFq3wgS2rSwvyncuQ6fzX8jwdoe28qWW1s',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    tone_analysis = tone_analyzer.tone(
        {'text': cleaned_tweets[0]},
        'application/json'
    ).get_result()
    return JsonResponse(tone_analysis, safe=False)




    #
    # return JsonResponse(tweets, safe=False)
