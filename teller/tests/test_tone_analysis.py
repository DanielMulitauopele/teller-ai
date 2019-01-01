from django.test import SimpleTestCase, TestCase
from watson_developer_cloud import ToneAnalyzerV3

from .. import tone_analysis


class AnalyzeToneViaWatsonTestCase(TestCase):
    def test_analyze_tone_via_watson_works(self):
        sentance = "Wow this totally works!"
        expected_result = { "document_tone": {
                                "tones": [
                                  {
                                    "score": 0.625141,
                                    "tone_id": "joy",
                                    "tone_name": "Joy"
                                  },
                                  {
                                    "score": 0.97759,
                                    "tone_id": "confident",
                                    "tone_name": "Confident"
                                  }
                                ]
                              }
                          }
        self.assertEqual(tone_analysis.analyze_tone_via_watson(sentance), expected_result)
