from twython import Twython as tw, TwythonStreamer as ts
from nltk.tokenize import word_tokenize as tokenize
import pandas as pd
import pymongo as pm
import json
from tweepy import OAuthHandler as oah
import tweepy
from tweepy import StreamListener
appKey = 'vadzcV4cnW0raDQq7oBzZNl08'
appSecret = 'l6npphvzjHNC4vIfMY7SMDgUPPQRwyDzyS7KhghqpWVkTOKerp'
accessToken = '872886602867126272-hNRkWRTlFLPe6vqCGz3oi8T8w1kKADS'
accessSecret = 'nf6shsNNDbrJgg6mR6JPFkyOyzdcy0bpBpbpl0aMmOlgP'
auth = oah(appKey, appSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('db.json', 'a') as f:
                print(data)
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


def tokenize():
    with open('db.json', 'r') as f:
        line = f.readline()  # read only the first tweet/line
        tweet = json.loads(line)  # load it as Python dict
        print(json.dumps(tweet, indent=4))  # pretty-print



def clear_DB():
    open('db.json', 'w').close()


def createStream():
    my_stream = MyStreamListener()
    twitter_stream = tweepy.Stream(auth=api.auth, listener=my_stream)
    twitter_stream.filter(track=['#python'])



def main():
    createStream()
    clear_DB()

    db.commit()
    db.close()

