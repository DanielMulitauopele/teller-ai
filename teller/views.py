import requests
from django.http import JsonResponse

import config
from . import tone_analysis, tweet_prep

def get_watson_analysis(request):
    coin = request.GET.get('coin') # Either returns the query param value, or returns "None"
    tweet_document = tweet_prep.prep_for_watson(coin)
    watson_tone_analysis = tone_analysis.analyze_tone_via_watson(tweet_document)

    return JsonResponse(watson_tone_analysis, safe=False)
