import os
from pymongo import MongoClient
import json
from bson.son import SON
import re
client = MongoClient('localhost', 27017)
db = client.tweet_database1
db.tweets1.drop()
tweets = db.tweets1
#print(client.list_database_names())

p = re.compile(r'\bhan\b|\bhon\b|\bden\b|\bdet\b|\bdenna\b|\bdenne\b|\bhen\b')
p1 = re.compile(r'\[(.*?)\]')
pth = "/home/ubuntu/tweets/"
tweets_ =  []
for root, dirs, files in os.walk(pth):
    for file in files:
        with open(pth+file) as f:
            for jsonObj in f:
                if len(jsonObj)>1:
                    tweet_ = json.loads(jsonObj)
                    if 'retweeted_status' not in tweet_:
                        tweet_ = {"text": tweet_['text'].lower()}
                        #print(tweet_)
                   # print(tweet_)
                        tweets_.append(tweet_)
                if len(tweets_) == 500000:
                    tweets.insert_many(tweets_)
                    tweets_ = []
                    print("insert data successfuly")
        if len(tweets_) != 0:
            tweets.insert_many(tweets_)
            tweets_ = []
            print("insert data succesfully")
print(tweets_ == [])
