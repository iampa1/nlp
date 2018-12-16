
# coding: utf-8

# In[6]:


import tweepy
from tkinter import *
from time import sleep
import numpy as np

#Authentication
consumer_key = 'ohNeoATMiza9SEIFhyF5qDnzf'
consumer_secret = 'eVqHVxY6jclkb8oFvZ3mSnoLQhdmxiDphSveRhDDSpAZ5EP8J8'
access_token = '580403542-7HLhWnqpcBrT1nMcOQo92dtkjJY4Jsss5XvHtxOx'
access_token_secret = 'm7LVRMCdyrBeseJ7pVPrJMKUSJcldlLi414RNb4MCgv2e'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
text=[]
time=[]
new_dict=dict()


keyword = input("Enter the keyword you want to search for ")

numberOfTweets = input("Enter the number of tweets you want")
numberOfTweets = int(numberOfTweets)
    
    

for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):
    try:
        print(tweet.text)
        global text
        text.append(tweet.text)
        global time
        time.append(tweet.created_at)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break


# In[11]:


text[2]


# In[19]:





# In[21]:





# In[22]:





# In[24]:





# In[25]:




