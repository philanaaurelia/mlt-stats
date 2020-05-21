import requests
import json 
import tweepy
import random
import os


class Tweet:
    def __init__(self, tweet,user,link):
        self.tweet = tweet
        self.user = user
        self.link = "http://twitter.com/"+ user +"/status/" + link
        
    def __str__(self):
        return "tweet: " + self.tweet +'\n' + "user: " + self.user + "\n" + "Link: " + self.link
        
def get_tweet():
    # twit_key = os.getenv('twit_key') - This is for Heroku
    twit_key = 'tMhwBBDqqeEiozlZVgCkzzCVO' 
    # twit_secret = os.getenv('twit_secret') - This is for Heroku
    twit_secret = 'LY7IzvOsVwlLyXv2X2dXo1Xy6MbbwAgL1DPUBrDQ7iTI2NTIQ4'
    auth = tweepy.OAuthHandler(twit_key, twit_secret)
    auth.set_access_token("1165427794815438848-j2xCg54UvzrAU4KQTZI7WOaL03bOF6","LFEJ61YW1C4px9T2QNl7ZjfasxfodGHMb8SccBjdwJ2rc")

    api = tweepy.API(auth)
    new_tweets = api.search(q="love Lauryn Hill -filter:retweets AND -filter:replies AND -filter:links AND -filter:twimg", count=100, lang="en")
    size = len(new_tweets)
    i = random.randint(0,size-1)
    text = json.dumps(new_tweets[i].text)
    text = text[1:-1]
    user = json.dumps(new_tweets[i].user.screen_name)
    user = user[1:-1]
    link = json.dumps(new_tweets[i].id_str)
    link = link[1:-1]
    randomtweet = Tweet(text,user,link)
    return randomtweet
    