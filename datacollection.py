#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import csv
import json
import datetime
import jsonpickle
import pandas as pd
from pymongo import MongoClient


# In[2]:


twitter_cred = dict()


# In[3]:


twitter_cred['CONSUMER KEY'] = 'UPeI5WvTfpJPBUBxmk0pqJv0p'
twitter_cred['CONSUMER_SECRET'] = 'VtRNMpaYVU36Ztfiu5wU4Yk7qBu1r5h4Gi1jaZAD21fA1UYB9Q'
twitter_cred['ACCESS KEY'] = '1175127666577592323-oVohjZ7E6cdIePo4G7zP3SDvIDktWj'
twitter_cred['ACCESS_SECRET'] = 'XHfu50AydSPWE9MRCpznNC0HkoFKIiZmSzmw51PoOrikS'


# In[4]:


with open('twitter_credentials.json','w') as secret_info:
    json.dump(twitter_cred, secret_info, indent = 4, sort_keys= True)


# In[5]:


with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    print(info)
    consumer_key = info["CONSUMER KEY"]
    consumer_secret = info["CONSUMER_SECRET"]
    access_key = info["ACCESS KEY"]
    access_secret = info["ACCESS_SECRET"]


# In[6]:


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)


# In[68]:


"""start_date = datetime.datetime(2019,10,5,0,0,0)
end_date = datetime.datetime(2019,10,8,0,0,0)
def get_tweets(filepath, api, query, max_tweets = 500, lang = 'en'):
    
    tweetCount = 0
    
    with open(filepath, 'a') as f:
        
        for tweet in tweepy.Cursor(api.search, q = query, lang = lang).items(max_tweets):
            if not tweet.retweeted and 'RT @' not in tweet.text:
           # if tweet.created_at > start_date and tweet.created_at < end_date:
                tweet_text = tweet.text
                time = tweet.created_at
                tweeter = tweet.user.screen_name
                tweet_dict= {"tweet_text":tweet_text.strip(),
                            "timestamp": str(time), "user" : tweeter}
                tweet_json = json.dumps(tweet_dict)
                f.write(jsonpickle.encode(tweet_json, unpicklable=False)+ '\n')
                tweetCount += 1
            
        print("downloaded {0} tweets".format(tweetCount))"""


# In[69]:


"""query = ['Hamza Choudhury','#LIVLEI']
get_tweets(r"C:\Users\what's in\Desktop\ds\tweets.json", api, query)"""


# In[7]:


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('race.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#MUNLIV','#UCL','#SHUARS','#NoRoomForRacism','#Lakers','#UEL','#NBA','#MCIAVL','#BURCHE','#SOULEI','#NORMUN','#ARSCRY'])
    

   
    
   


# In[9]:


with open(r"C:\Users\what's in\Desktop\ds\race.json",'r') as f:
    data = json.load(f)
df = pd.DataFrame.from_dict(data,orient="index")


# In[ ]:




