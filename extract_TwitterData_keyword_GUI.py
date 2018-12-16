
# coding: utf-8

# In[1]:


import tweepy
from tkinter import *
from time import sleep
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt

#Authentication
consumer_key = 'ohNeoATMiza9SEIFhyF5qDnzf'
consumer_secret = 'eVqHVxY6jclkb8oFvZ3mSnoLQhdmxiDphSveRhDDSpAZ5EP8J8'
access_token = '580403542-7HLhWnqpcBrT1nMcOQo92dtkjJY4Jsss5XvHtxOx'
access_token_secret = 'm7LVRMCdyrBeseJ7pVPrJMKUSJcldlLi414RNb4MCgv2e'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#GUI
root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label(root, text="Sample Size")
E2 = Entry(root, bd =5)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getData():
    getE1()
    keyword = getE1()

    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)

    #Where the tweets are stored to be plotted
    

    for tweet in tweepy.Cursor(api.search, keyword, lang="en").items(numberOfTweets):
        try:
            print(tweet.text)
            

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

submit = Button(root, text ="Submit", command = getData)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
submit.pack(side =BOTTOM)

root.mainloop()

