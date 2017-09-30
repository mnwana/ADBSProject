from twython import Twython as tw, TwythonStreamer as ts
global twitter
global data
global key
global token
# def setup():
#     appKey = 'vadzcV4cnW0raDQq7oBzZNl08'
#     appSecret = 'vadzcV4cnW0raDQq7oBzZNl08'
#     oauthToken = 'vadzcV4cnW0raDQq7oBzZNl08'
#     oauthSecret = 'vadzcV4cnW0raDQq7oBzZNl08'
#     #twitter = twython.Twython(appKey, appSecret, oauthToken, oauthSecret)
#     #print(twitter.search(q='hack this'))
# def pullTweets():
#     tmln=twitter
#
#
# def setupAPI():
#     key = 'vadzcV4cnW0raDQq7oBzZNl08'
#     twitter = twython.Twython(key, key, oauth_version=2)
#     token=twitter.obtain_access_token()
#     twitter = twython.Twython(key, access_token=token)
#
# class streamer(twython.TwythonStreamer):
#     def on_success(self, data):
#         if 'text' in data:
#             print (data['text'].encode('utf-8'))
#
#     def on_error(self, status_code, data):
#         print (status_code)
#
#         # Want to stop trying to get data because of the error?
#         # Uncomment the next line!
#         self.disconnect()
# def main():
#     setup2()
#     stream = streamer(key, key, key, key)
#     stream.statuses.filter(track='twitter')


def setup_key():
    appKey= appSecret = 'vadzcV4cnW0raDQq7oBzZNl08'

    twitter = tw(appKey, appSecret, oauth_version=2)
    token = twitter.obtain_access_token()
    twitter = tw(appKey, access_token=token)


def setup_stream():
    complex


class streamer(ts):
    def on_success(self, data):
        if 'text' in data:
            print (data['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print (status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()


def main():
    setup_key()



main()