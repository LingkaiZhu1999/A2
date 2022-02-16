#!/usr/bin/env python3
"""mapper.py"""
import re
import sys
import json
# \b allows you to perform a “whole words only” search using a regular expression in the form of \bword\b.
count = 0 # number of unique tweets.
p = re.compile(r'\bhan\b|\bhon\b|\bden\b|\bdet\b|\bdenna\b|\bdenne\b|\bhen\b')
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
    if len(line) > 1:
        tweet_json = json.loads(line)
        # print(tweet_json['text'])
        if 'retweeted_status' not in tweet_json:
            # In this analysis, only unique tweets should be taken into account, i.e. ‘retweets’ should be disregarded
            tweet_text = tweet_json['text']
            count = count + 1
            tweet_text = tweet_text.lower()
            if p.findall(tweet_text) != None:
                pronoun = p.findall(tweet_text)
                for element in pronoun:
                    print('%s\t%s' % (element, 1))
