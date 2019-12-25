import unittest
from scrapers import get_tweets

class TestTwitterFunc(unittest.TestCase):
    
    def test_twitter_get_tweets(self):
        user = 'realDonaldTrump'
        tweets = list(get_tweets(query=user, pages=1))
        print(type(tweets))
        print(tweets)
        print(len(tweets))
        for t in tweets:
            print(t)
            print(t['tweetId'])
        self.assertTrue(tweets[0].__contains__('tweetId'))
        print("test_twitter_get_tweets 测试结束")
if __name__ == '__main__':
    unittest.main()
