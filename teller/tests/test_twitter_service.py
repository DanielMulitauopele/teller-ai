import json

from django.test import TestCase
from rest_framework import status

from .. import twitter_service


class GetTwitterService(TestCase):
    def test_get_all_twitter_data(self):
        query = 'dogecoin'
        twitter_response = twitter_service.retrieve_twitter_data(query)

        self.assertNotEqual(twitter_response, None)
