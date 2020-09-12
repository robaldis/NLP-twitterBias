# twitterUserFinder.py
from __future__ import unicode_literals
import tweepy
from dotenv import load_dotenv
import time
import os
import pickle

load_dotenv()
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

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print(f"Rate limit has been reached at {time.ctime(time.time())}")
            time.sleep((15 * 60) + 2)
            print("Wait time complete")
        except StopIteration:
            return
        except tweepy.TweepError:
            print("Can't get this information skipping the user")
            return

def getUser(userList, iterations):

    for i in range(iterations):
        newUser = []
        for user in userList:
            for follower in limit_handler(tweepy.Cursor(api.friends_ids, user_id=user).items()):
                newUser.append(follower)

        userList += newUser
        userList = list(set(userList))
        userList.sort()
    return userList
    
def getTweets(userId, count):
    page = 1
    deadend = False
    tweets = []
    lenPrev = 0
    try:
        while True:
            for tweet in tweepy.Cursor(api.user_timeline,user_id=userId,page=page, tweet_mode="extended").items():
                tweets.append(tweet)
            if len(tweets) < count and len(tweets) > lenPrev:
                lenPrev = len(tweets)
                print ("Getting more posts")
            else:
                print("Deadend reached")
                deadend = True
                
                userDict = {
                    userId: tweets
                }
                return userDict
            if not deadend:
                page += 1
                time.sleep(1)
    except tweepy.TweepError:
            print(f"Rate limit reached at {time.ctime(time.time())}")
            time.sleep((15*60)+2)
            print("Continuing to find tweets")
    userDict = {
        userId: tweets
    }
    return userDict




if __name__ == "__main__":
    # tweetDataset = []
    userList = getUser([936664960494718976], 2)
    print("finished getting accounts")
    for user in userList:
        userDict = getTweets(user, 1000)
        # tweetDataset.append(userDict)
        pickle.dump(userDict, open(f"twitterBias/tweets/{user}.p", "wb"))
    pass