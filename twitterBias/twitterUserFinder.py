# twitterUserFinder.py
import tweepy
from dotenv import load_dotenv
import os

# Get all the information to connect to the twitter api.
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Setup authentication to connect to the twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Connect with the twitter api
api = tweepy.API(auth)

def getUser(userList, iterations):
    for i in iterations:
        newUsers = []
        for user in userList:
            # append the new user list to the newUser list
            newUsers.append(api.followers(user))
            break

        userList.append(newUsers)
        #sort get rid of duplicates and sort the array
        userList = list(dict.fromkeys(userList))
        userList.sort()
    return userList


    if __name__ == "__main__":
        getUser('robertaldis', 2)
        pass