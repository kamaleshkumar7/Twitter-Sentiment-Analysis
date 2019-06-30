import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key= 'vf10Ckf8d8plWcMc2ypnsnD90'
consumer_secret= 'hvSFHvZbudnVXJdoR4XEqhWRaPvv22dWLezK1int5Mz0Xf87VA'

access_token='740565057243750401-vn5CJlI5AOQWyFqAlzQj3NJJjiTXhee'
access_token_secret='EEGwpCMDZ9HqPd3rLdz0LCyyKWFjDJOTyoamZ7mzYwQZD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
keyword = input("Enter Keyword ")
public_tweets = api.search(keyword)

csvFile = open('result.csv', 'a')

csvWriter = csv.writer(csvFile)

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


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