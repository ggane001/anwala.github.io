from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json
import re

class listener(StreamListener):
    
    def __init__(self, api=None):
        super(listener, self).__init__()
        self.num_tweets = 0

    def on_data(self,data):        
        #print (data)
        
        if self.num_tweets < 2001:
            tweet = json.loads(data)
            for url in tweet["entities"]["urls"]:
                if('twitter.com' not in url["expanded_url"]):
                    self.num_tweets += 1
                    fileToStoreListOfUrls.write(url["expanded_url"] + '\n')
                    print(self.num_tweets)
            return True
        else:
            print('Exception')
           
            return False
        
    def on_error(self, status):
        print(status)
        
fileToStoreListOfUrls = open("C:\ListOfUrls.txt","a+")
auth = tweepy.OAuthHandler('sXBU4507CXpRMqo229oBxDzPP', 'U9HiwDJVtLz57vpb1jRbfr5gVlrMRARf2YEjeD9klE6Sjiyayq')
auth.set_access_token('755808986977501184-5U4n5I6ioaak7Ja5Lb0n8ZgADCCnQaW', 'xj1Pjwholos0e4eeSTSlb8QdIgJoYhxKhlxNIDeeLO5G4')
twitterStream = Stream(auth,listener())
twitterStream.filter(track=['sports','music','awards','NASA','cricket','arts','nature','computers','gardening','genetics','medicine'])
fileToStoreListOfUrls.close()
print ('Completed Streaming.')
