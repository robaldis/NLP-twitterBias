# twitterUserFinder.py
from __future__ import unicode_literals
import tweepy
from dotenv import load_dotenv
import time
import os

# Get all the information to connect to the twitter api.
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Setup authentication to connect to the twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Connect with the twitter api
api = tweepy.API(auth)
def getUser(userList, iterations):
    for user in tweepy.Cursor(api.followers,screen_name="RobertAldis").items(10):
        try:
            # user = next(users)
            print(user.screen_name)
        except tweepy.TweepError:
            print("tweepy has reached its rate limit for now")
            time.sleep(60 * 15)
            print(user.screen_name)
            # next(users)
    # print(userList)
    # for i in range(iterations):
    #     newUsers = []
    #     for user in userList:
    #         print(user)
    #         # append the new user list to the newUser list
    #         newUsers.append(api.followers(user))
    #         break

    #     userList.append(newUsers)
    #     #sort get rid of duplicates and sort the array
    #     userList = list(dict.fromkeys(userList))
    #     userList.sort()
    # return userList


if __name__ == "__main__":
    getUser([], 2)
    pass