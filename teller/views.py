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

    for tweet in tweets:
    # tweet = "we're they're our I'm I'll would've could've should've"
    # CLEAN TWEET CONTRACTIONS
        contractions = {"'s":"is", "'re":"are", "'ve":"have", "'nt":"not", "'d":"would", "'m":"am", "'ll":"will"}
        poss_contractions = tweet.replace("'", " '").split(" ")
        for poss_contraction in poss_contractions:
            non_contraction = [contractions[poss_contraction] if poss_contraction in contractions else poss_contraction for poss_contraction in poss_contractions]

            sentance = ' '.join(non_contraction)
            # CLEAN HASHTAGS
            tweet = sentance.replace("#", "")





    # tone_analyzer = ToneAnalyzerV3(
    #     version='2017-09-21',
    #     iam_apikey='Si1t19DXhzGFq3wgS2rSwvyncuQ6fzX8jwdoe28qWW1s',
    #     url='https://gateway.watsonplatform.net/tone-analyzer/api'
    # )
    #
    # # text = 'I am so in love with the Watson API, although it was a long and arduous process getting this thing established. I wish the documentation was more nuanced, especially in regards to junior developers. Its frustrating slogging through unhelpful docs.'
    #
    # tone_analysis = tone_analyzer.tone(
    #     {'text': text},
    #     'application/json'
    # ).get_result()
    return JsonResponse(tweets, safe=False)




    #
    # return JsonResponse(tweets, safe=False)
