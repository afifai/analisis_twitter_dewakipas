from config import api
from time import sleep
import csv

keywords = ['dewa kipas', 'dadang subur', 'irene sukandar',
            'dadang irene']
f = open('data_tweet.csv', 'a', newline='')
fieldnames = ['id', 'timestamp', 'name', 'tweets', 'loc']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
f.close()
while True:
    for k in keywords:
        tweets = api.search(k, count=100, tweet_mode='extended')
        for item in tweets:
            if (not item.retweeted) and ('RT @' not in item.full_text):
                with open('data_tweet.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'id': item.id_str,
                                     'timestamp': item.created_at,
                                     'name': item.user.screen_name,
                                     'tweets': item.full_text,
                                     'loc': item.user.location})
        sleep(2)
    sleep(60)
