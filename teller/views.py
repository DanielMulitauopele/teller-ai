from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from watson_developer_cloud import ToneAnalyzerV3
import requests
import config
from . import tweet_prep

class WelcomePageView(TemplateView):
    def get(self, request):
        return render(request, 'welcome.html')

def analyze_tone_via_watson(document):
    tone_analyzer = ToneAnalyzerV3(
                        version='2017-09-21',
                        iam_apikey=f'{config.watson_key}',
                        url='https://gateway.watsonplatform.net/tone-analyzer/api'
                        )
    result = tone_analyzer.tone(
                {'text': document},
                'application/json',
            ).get_result()
    return result

def watson_analysis(request):
    coin = request.GET.get('coin') # Either returns the query param value, or returns "None"
    tweet_document = tweet_prep.prep_for_watson(coin)
    tone_analysis = analyze_tone_via_watson(tweet_document)

    return JsonResponse(tone_analysis, safe=False)
