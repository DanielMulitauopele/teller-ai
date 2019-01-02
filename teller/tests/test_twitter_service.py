import json

from django.test import TestCase
from rest_framework import status

from .. import twitter_service


class GetTwitterService(TestCase):
    def test_get_all_twitter_data(self):
        query = 'dogecoin'
        twitter_response = twitter_service.retrieve_twitter_data(query)

        self.assertNotEqual(twitter_response, None)
        self.assertFalse('statuses' in twitter_response)
        self.assertTrue('text' in twitter_response[0])
        self.assertTrue('created_at' in twitter_response[0])
        self.assertTrue('user' in twitter_response[0])
        self.assertTrue('name' in twitter_response[0]['user'])
        self.assertTrue('screen_name' in twitter_response[0]['user'])
