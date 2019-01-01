import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

client = Client()

class GetWatsonSentimentAnalysis(TestCase):
    def test_get_all_sentiments(self):
        response = client.get(reverse('watson_analysis'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetWelcomePage(TestCase):
    def test_get_welcome_page(self):
        response = client.get(reverse('welcome'))

        self.assertEqual(response.status_code, 200)
