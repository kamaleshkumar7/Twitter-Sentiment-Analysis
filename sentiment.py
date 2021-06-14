import tweepy
from textblob import TextBlob
import csv

consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
keyword = input("Enter Keyword ")
public_tweets = api.search(keyword)

csvFile = open('result.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in public_tweets:
    print(tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if(analysis.sentiment.polarity < 0):
    	print("negative")
    elif(analysis.sentiment.polarity>0):
    	print("positive")
    else:
    	print("neutral")
    print("")
