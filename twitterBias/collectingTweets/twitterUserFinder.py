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

# Prevents from accessing the API too much to get timed out
# There is a 15minute cool down after 200 requests to the API
def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print(f"Rate limit has been reached at {time.ctime(time.time())}")
            # wait 2 seconds longer than 15 minutes just to be safe
            time.sleep((15 * 60) + 2)
            print("Wait time complete")
        except StopIteration:
            return
        except tweepy.TweepError: # If the users account cant be accessed due to privacy settings most likely
            print("Can't get this information skipping the user")
            return

# Gets all the user for a specific user list and how many iterations deep they want to go in the friends list
# for example 2 iterations to get friends of friends and so on.
def getUser(userList, iterations):
    '''Gets all the users friends ID's and thier friends basedd on the iteration level. '''
    for i in range(iterations):
        newUser = []
        for user in userList:
            # Get all the users freinds unless it is being limited by the rate limit.
            for follower in limit_handler(tweepy.Cursor(api.friends_ids, user_id=user).items()):
                newUser.append(follower)

        userList += newUser
        # Gets rid of duplicates in the list
        userList = list(set(userList))
        userList.sort()
    return userList



def getTweets(userId, count):
    '''Gets the tweets of all ther users ID in a list'''
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
    userList = getUser([936664960494718976], 2)
    print("finished getting accounts")
    for user in userList:
        userDict = getTweets(user, 1000)
        # Pickles all of the information into seperate files so the it doesn't overload the memory
        pickle.dump(userDict, open(f"twitterBias/tweets/{user}.p", "wb"))
    pass