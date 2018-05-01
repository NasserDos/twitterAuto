from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB
from tweepy.streaming import json

client = MongoClient('localhost', 27017)
db = client.tweets


def insertTweetsToMongo(tweets):
    """
    inserts a json into our collection in mongo
    :param json:
    :return:
    """
    for tweet in tweets:
        result = db.tweets.insert_one(tweet._json)

    print("Completed JSON inserts")
