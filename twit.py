import requests
import json 
import tweepy
import random
import os


class Tweet:
    def __init__(self, tweet,user,link):
        self.t = tweet
        self.u = user
        self.l = "http://twitter.com/"+ user +"/status/" + link
        
    def __str__(self):
        return "tweet: " + self.t +'\n' + "user: " + self.u + "\n" + "Link: " + self.l
        
def get_tweet():
    # twit_key = os.getenv('twit_key')
    twit_key = 'UjvHcugOaomXcIeN600OTd56e'
    # twit_secret = os.getenv('twit_secret')
    twit_secret = 'GrmnaT8HNlNFH2pF98ScPecF49RM470CSWnWVNMj7FAr60biq9'
    auth = tweepy.OAuthHandler(twit_key, twit_secret)
    auth.set_access_token("57044214-C3qKJQCHr9Ez0hOEnBDcvvQVNOFjHyKmA2ymLoDUI","XnCr2df78uAs4QCdDdBDi3RzSL9d9jBBIw5ExXdXi5Hcc")

    api = tweepy.API(auth)
    new_tweets = api.search(q="love Lauryn Hill -filter:retweets AND -filter:replies AND -filter:links AND -filter:twimg", count=100, lang="en")
    size = len(new_tweets)
    # print("these are the tweets %s", new_tweets[1])
    i = random.randint(0,size)
    text = json.dumps(new_tweets[i].text)
    text = text[1:-1]
    user = json.dumps(new_tweets[i].user.screen_name)
    user = user[1:-1]
    link = json.dumps(new_tweets[i].id_str)
    link = link[1:-1]
    randomtweet = Tweet(text,user,link)
    return randomtweet
    