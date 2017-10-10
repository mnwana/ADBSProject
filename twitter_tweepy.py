import tweepy
from textwrap import TextWrapper
from elasticsearch import Elasticsearch

consumer_key = 'vadzcV4cnW0raDQq7oBzZNl08'
consumer_secret = 'l6npphvzjHNC4vIfMY7SMDgUPPQRwyDzyS7KhghqpWVkTOKerp'
access_token = '872886602867126272-hNRkWRTlFLPe6vqCGz3oi8T8w1kKADS'
access_secret= 'nf6shsNNDbrJgg6mR6JPFkyOyzdcy0bpBpbpl0aMmOlgP'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

es = Elasticsearch()
es.indices.create(index="twitter_index")

class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:

            json_data = status._json
            print(json_data['text'])

            es.create(index="idx_twp",
                      doc_type="twitter_twp",
                      body=json_data
                      )

        except Exception as e:
            print(e)
            pass

streamer = tweepy.Stream(auth=auth, listener=StreamListener())

#Fill with your own Keywords bellow
terms = ['python']

streamer.filter(None, terms)
streamer.disconnect()
