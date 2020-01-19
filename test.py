import unittest
from scrapers import get_tweets
from scrapers import DingDing
class TestTwitterFunc(unittest.TestCase):

    access_token="8742ed4f6aa415d3d61b26a41ae3b5d80effbb3db9cb162c71ba938945ff79af"
    ding = DingDing(access_token)
    ding.send_text('hello', at_all=False)
    def test_twitter_get_tweets(self):
        user = 'realDonaldTrump'
        tweets = list(get_tweets(query=user, pages=2))
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
