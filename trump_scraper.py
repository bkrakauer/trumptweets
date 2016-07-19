# Thanks to Yanofsky

import settings
import tweepy
import csv

auth = tweepy.OAuthHandler(settings.APP_KEY, settings.APP_SECRET)
auth.set_access_token(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

all_tweets = []

new_tweets = api.user_timeline(screen_name = "realdonaldtrump", count = 20000)
all_tweets.extend(new_tweets)
oldest = all_tweets[-1].id - 1 

while len(new_tweets) > 0:
	new_tweets = api.user_timeline(screen_name = "realdonaldtrump", count = 200, max_id = oldest)
	all_tweets.extend(new_tweets)
	oldest = all_tweets[-1].id - 1
	
print "Downloaded %s tweets." %(len(all_tweets))
outtweets = [[tweet.text.encode("utf-8"), tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.id_str] for tweet in all_tweets]

with open('trump_tweets2.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["text","created_at","favorite_count","retweet_count","id"])
	writer.writerows(outtweets)
	
	pass
