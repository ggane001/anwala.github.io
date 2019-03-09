import tweepy
from tweepy import OAuthHandler
import json
import urllib
import csv
import time

auth = tweepy.OAuthHandler('sXBU4507CXpRMqo229oBxDzPP', 'U9HiwDJVtLz57vpb1jRbfr5gVlrMRARf2YEjeD9klE6Sjiyayq')
auth.set_access_token('755808986977501184-5U4n5I6ioaak7Ja5Lb0n8ZgADCCnQaW', 'xj1Pjwholos0e4eeSTSlb8QdIgJoYhxKhlxNIDeeLO5G4')
api = tweepy.API(auth)

users = tweepy.Cursor(api.friends, screen_name="acnwala").items()
with open("C:\\acnwala_twitter_follows_count.csv", "w", newline='') as acnwala_twitter:
    writer = csv.writer(acnwala_twitter)
    currentData = ['UserName','FollowsCount']
    writer.writerow(currentData)
    while True:
        try:
            user = next(users)
            #users_current = tweepy.Cursor(api.friends, screen_name=user.screen_name).items()
        except tweepy.TweepError:
            print(tweepy.TweepError)
            time.sleep(60*15)
            user = next(users)
        except StopIteration:
            break
        currentData = [user.screen_name,user.friends_count]
        writer.writerow(currentData)
print('Completed.')