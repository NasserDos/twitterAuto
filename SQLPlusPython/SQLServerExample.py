import pyodbc
from datetime import datetime

from SQLPlusPython.HelperFunctions import *

## All the information you use to connect to your SQL Server database today
server = '40.65.111.217'
database = 'nasserbinshabeeb'
username = 'nasserbinshabeeb'
password = 'kelkoo.tough.lists'

connectionString = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database
connectionString = connectionString + ';UID=' + username + ';PWD=' + password

## Create a connection
connection = pyodbc.connect(connectionString)
openConnection = connection.cursor()

# Create Table if does not exist
createTable = "IF NOT EXISTS (SELECT * FROM sys.tables T WHERE T.name = 'Tweets')" \
              "BEGIN " \
              "CREATE TABLE Tweets(" \
              "	TweetID int IDENTITY(1,1) PRIMARY KEY NOT NULL," \
              "OriginTweetID bigint, " \
              "TweetSource varchar(255) ," \
              "TweetText varchar(255)," \
              "TweetDate datetime," \
              "Retweets int," \
              "Favorites int," \
              "SentimentScore int ," \
              "TweetJSON varchar(max)" \
              ")" \
              " END"

openConnection.execute(createTable)
openConnection.commit()


## Writes some data down to a table called SampleTable that has two values - one varchar, one
##  int.  The ? represent parameters.  args below is a list that has each of the parameters you
##  want passed in

def insertTweetsToSQL(tweets):
    """
    Inserts Tweets into sql server database
    :param tweets: the list of tweets
    :return: nil
    """
    insertConnection = pyodbc.connect(connectionString)
    tempConnection = insertConnection.cursor()
    for tweet in tweets:
        sqlString = 'INSERT Tweets (OriginTweetID, TweetSource,TweetText,TweetDate, Retweets, Favorites, ' \
                    'SentimentScore,TweetJSON) VALUES (?,?,?,?,?,?,?,?) '
        args = int(tweet.id), str(tweet.source), str(tweet.text), tweet.created_at, int(tweet.retweet_count), \
               tweet.favorite_count, analize_sentiment(tweet.text), str(tweet._json)
        tempConnection.execute(sqlString, args)
    print("Completed SQL inserts")
    tempConnection.commit()
    tempConnection.close()
    insertConnection.close()

def getAverageSentiment():
    """
    handles the sentiment calculation
    :return:
    """
    myConnection = pyodbc.connect(connectionString)
    tempConnection = myConnection.cursor()
    sqlString = "SELECT SUM(SentimentScore) [aTotal], COUNT(SentimentScore) [aCount] FROM Tweets"
    res = tempConnection.execute(sqlString)
    tot, count = res.fetchone()

    return tot/count

## Clean up after yourself
openConnection.close()
connection.close()
