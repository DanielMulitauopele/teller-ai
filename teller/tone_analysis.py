import os
import requests
from django.http import JsonResponse

from watson_developer_cloud import ToneAnalyzerV3


def analyze_tone_via_watson(document):
    tone_analyzer = ToneAnalyzerV3(
                        version='2017-09-21',
                        iam_apikey=f'{os.environ.get("watson_key")}',
                        url='https://gateway.watsonplatform.net/tone-analyzer/api'
                        )
    result = tone_analyzer.tone(
                {'text': document},
                'application/json',
            ).get_result()
    tone_names = []
    raw_tones = result['document_tone']['tones']
    for raw_tone in raw_tones:
        tone_names.append(raw_tone['tone_id'])
    return { 'document_tones': tone_names }
