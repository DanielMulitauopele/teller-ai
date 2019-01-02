import requests
from django.http import JsonResponse

from watson_developer_cloud import ToneAnalyzerV3

import config

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
