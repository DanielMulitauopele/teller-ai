from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages
from watson_developer_cloud import ToneAnalyzerV3
import requests
import config

class WelcomePageView(TemplateView):
    def get(self, request):
        return render(request, 'welcome.html')

def prep_tweets(coin):
    data = retrieve_twitter_data(coin)
    tweets = retrieve_raw_tweets(data)
    cleaned_tweets = clean_for_watson_analysis(tweets)
    return create_document(cleaned_tweets)

def retrieve_twitter_data(query):
    url = f'https://api.twitter.com/1.1/search/tweets.json?q={query}&lang=en&count=100&result_type=recent'
    headers = {'authorization': f'Bearer {config.twitter_token}'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['statuses']

def retrieve_raw_tweets(statuses):
    raw_tweets = []
    for status_info in statuses:
        raw_tweets.append(status_info['text'])
    return raw_tweets

def clean_for_watson_analysis(tweets):
    clean_tweets = []
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

        clean_tweets.append(tweet)
    return clean_tweets

def create_document(tweets):
    return ' '.join(tweets)

def watson_analysis(request):
    coin = request.GET.get('coin') # Either returns the query param value, or returns "None"
    tweet_document = prep_tweets(coin)

    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey=f'{config.watson_key}',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    tone_analysis = tone_analyzer.tone(
        {'text': tweet_document},
        'application/json',
    ).get_result()

    return JsonResponse(tone_analysis, safe=False)
    # return JsonResponse(tweet_document, safe=False)
