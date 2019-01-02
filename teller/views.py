import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import config
from . import tone_analysis, tweet_prep


class WelcomePageView(TemplateView):
    def get(self, request):
        return render(request, 'welcome.html')

def get_watson_analysis(request):
    coin = request.GET.get('coin') # Either returns the query param value, or returns "None"
    tweet_document = tweet_prep.prep_for_watson(coin)
    watson_tone_analysis = tone_analysis.analyze_tone_via_watson(tweet_document)

    return JsonResponse(watson_tone_analysis, safe=False)