#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
import os
import re

pth = "/home/ubuntu/tweets"
p = re.compile(r'\bhan\b|\bhon\b|\bden\b|\bdet\b|\bdenna\b|\bdenne\b|\bhen\b')
# \b allows you to perform a “whole words only” search using a regular expression in the form of \bword\b.
#han = r'\b(?:han)\b'
#hon = r'\b(?:hon)\b'
#den = r'\b(?:den)\b'
#det = r'\b(?:det)\b'
#denna = r'\b(?:denna)\b'
#denne = r'\b(?:denne)\b'
#hen = r'\b(?:han)\b'
# json.loads() takes a JSON encoded string, not a filename. You want to use json.load() (no s) instead and pass in an open file object:
# for root, dirs, files in os.walk(pth):
#     for file in files:
#        # print(file)
#         with open(os.path.join(pth, file), errors='ignore') as f:
#             for line in f:
#                 if len(line) >4:
#                     tweet_json = json.loads(line)
#                    # print(tweet_json['text'])
#                     if tweet_json['retweet_count'] == 0:
#                         tweet_text = tweet_json['text'] # In this analysis, only unique tweets should be taken into account, i.e. ‘retweets’ should be disregarded
#                         if p.search(tweet_text) != None:
#                             pronoun = p.search(tweet_text).group(0)
#
#                             print('%s\t%s' % (pronoun, 1))
#                # print(line)
               # line = json.dumps(line)
               # print(line)
               # tweet_json = json.loads(line)
                #for key, value in tweet_json.keys():
                #    print(k, value
            # print(data)
            # json_data = json.loads(data)
       # print(data)
       # print("********************")
            #print(json_data['text'])
               # print(element)
               # text_temp = json_data[k]['text']
               # print(text_temp)
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    # line = line.strip()
    # # split the line into words
    # words = line.split()
    # # increase counters
    # for word in words:
    #     # write the results to STDOUT (standard output);
    #     # what we output here will be the input for the
    #     # Reduce step, i.e. the input for reducer.py
    #     #
    #     # tab-delimited; the trivial word count is 1
    #     print('%s\t%s' % (word, 1))
    if len(line) > 4:
        tweet_json = json.loads(line)
        # print(tweet_json['text'])
        if tweet_json['retweet_count'] == 0:
            # In this analysis, only unique tweets should be taken into account, i.e. ‘retweets’ should be disregarded
            tweet_text = tweet_json['text']
            if p.findall(tweet_text) != None:
                pronoun = p.findall(tweet_text)
                print('%s\t%s' % (pronoun, 1))
