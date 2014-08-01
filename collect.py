import urllib2

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from settings import *


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        twitter_mention_url = "{0}{1}".format(STREAM_SERVER, '/api/twitter-mentions/')
        # print twitter_mention_url
        request = urllib2.Request(twitter_mention_url, data, {'Content-Type': 'application/json'})
        urllib2.urlopen(request).read()

        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, l)
    stream.filter(track=['DevTeam1Percent', '1percentclub',])