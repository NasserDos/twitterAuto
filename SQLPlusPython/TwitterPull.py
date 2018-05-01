import tweepy
from tweepy import OAuthHandler
from SQLPlusPython.SQLServerExample import *
from SQLPlusPython.MongoDBExample import *

## All the important information you were asked to collect from Twitter

twitterKey = 'N8DgUGDSfXdjB4OakhLzKRmQX'
twitterSecret = '3BF95TuLCZ2faisL9YpVISCQow1O58Pg64WHJ75RUmm1i61uel'
accessToken = '986055587220746241-6aOU6It3rUDi7B1ordOMjdiMRm79Q5q'
accessSecret = 'c3gnPZ5OlMtqi3eiARXVYuPwFgmvmbTYyaPxOqMkZGAjW'

##Authenticate your app
auth = OAuthHandler(twitterKey, twitterSecret)
auth.set_access_token(accessToken, accessSecret)

## Opens a connection to twitter - respecting rate limits (so you don't get stopped
apiAccess = tweepy.API(auth, wait_on_rate_limit=True)

## q is your search string.  lang is the language you want.  count tells the system how much to 
##  bring back per call.  .items takes a value that represents the total number of items you 
##  want back.


tweets = tweepy.Cursor(apiAccess.search, q='#godofwar', count=150, lang='en').items(150)


def Requirements():
    """
    inserts tweets into dbs
    :return:
    """
    insertTweetsToMongo(tweets)
    insertTweetsToSQL(tweets)
    sentimentAverage = getAverageSentiment()

    print("Sentiment Average :", sentimentAverage)


