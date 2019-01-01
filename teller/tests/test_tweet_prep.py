from django.test import TestCase

from .. import tweet_prep

class TweetPrepTestCase(TestCase):
    def test_extract_raw_tweets(self):
        example_twitter_response = [{  "created_at": "Tue Jan 01 22:45:06 +0000 2019",
                                        "id": 1080233483493171200,
                                        "id_str": "1080233483493171200",
                                        "text": "The dogecoin market makes this exchanger fabulous January 01, 2019 at 04:45PM $BTC $LTC $USDT $DASH $DOGE $ETH $BCH https://t.co/Ixqd2BHu7B",
                                        "user": {
                                            "id": 1017111153955106816,
                                            "id_str": "1017111153955106816",
                                            "name": "Satoshi Models",
                                            "screen_name": "SatoshiModels",
                                            }
                                    },
                                    {   "created_at": "Tue Jan 01 22:29:55 +0000 2019",
                                        "id": 1080229662855495680,
                                        "id_str": "1080229662855495680",
                                        "text": "RT @cryptoknocks: BTC-DOGE AskRate: 0.00000063 #Bittrex  #DOGE $DOGE #Dogecoin #altcoin #altcoins #cryptocurrencies\n ♥ FOLLOW for PROFIT",
                                        "user": {
                                            "id": 922843591231311872,
                                            "id_str": "922843591231311872",
                                            "name": "Cryptoknocks.com",
                                            "screen_name": "cryptoknocks",
                                            }
                                    }]

        actual = tweet_prep.extract_raw_tweets(example_twitter_response)
        expected = ["The dogecoin market makes this exchanger fabulous January 01, 2019 at 04:45PM $BTC $LTC $USDT $DASH $DOGE $ETH $BCH https://t.co/Ixqd2BHu7B",
                   "RT @cryptoknocks: BTC-DOGE AskRate: 0.00000063 #Bittrex  #DOGE $DOGE #Dogecoin #altcoin #altcoins #cryptocurrencies\n ♥ FOLLOW for PROFIT"]
        self.assertEqual(actual, expected)
