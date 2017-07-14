# -*- coding: utf-8 -*-
# Bot includes some non-English characters, for fun (: 

import tweepy
from time import sleep
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

while True:
    public_tweets = api.home_timeline(count=5)  # Getting the latest 5 tweets from user's timeline

    for tweet in public_tweets:
        twee_len = len(tweet.text)
        condition = "։".decode('utf-8')  # ' : ' is different from ' ։ '
        sn = tweet.user.screen_name.encode('utf-8')
        status_y = "@%s %s նիշ, վերջակետով" % (sn, twee_len)
        status_n = "@%s %s նիշ, առանց վերջակետ" % (sn, twee_len)
        try:
            # avoiding tweets that are retweets of our user's own tweets. 
            # To avoid possible infinite loop

            if tweet.text[0:2] != "RT" and sn != "armRTbot":
                if tweet.text[twee_len - 1] == condition:
                    print tweet.text
                    print status_y
                    api.update_status(status_y, tweet.id)
                    print
                else:
                    print tweet.text
                    print status_n
                    api.update_status(status_n, tweet.id)
                    print
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)

        sleep(3600)  # wait for an hour.    
