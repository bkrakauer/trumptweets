# Thanks to Yanofsky

import settings
import tweepy
import csv

auth = tweepy.OAuthHandler(settings.APP_KEY, settings.APP_SECRET)
auth.set_access_token(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#tweets to look at -- ...7488 is the Pence announcement.
# ...7920 complains about 'crooked hillary's' ads.
# ...5072 is about Obama and Israel
# ...6864 is the response to Hillary's 'Delete your account' (and his most popular) 
# ...1360 is about an event in NH
# ...8368 is an attack on Jeb
# ...0865 is about a poll
# ...5825 is defensive abt donating to veterans
# ...4577 is an attack on the media
# ...4864 is about debate performance
# ...2192 complains abt negative ads / winning in FL

tweet_set = [754136526087487488, 753353898472017920, 753349911983235072, 741007091947556864, \
696085979560591360, 690701138899898368, 689956187434020865, 734938503541325825, 735125552064024577, \
698751641873444864, 710151964726792192]

all_tweets = []

for tweetid in tweet_set:
	new_tweets = api.retweets(id=tweetid, count = 200)
	all_tweets.extend(new_tweets)
	oldest = all_tweets[-1].id - 1 

	while len(new_tweets) > 0:
		new_tweets = api.retweets(id = tweetid, count = 200, max_id = oldest)
		all_tweets.extend(new_tweets)
		oldest = all_tweets[-1].id - 1
	
print "Downloaded %s retweets." %(len(all_tweets))

outtweets = [[tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')] for tweet in all_tweets]

with open('trumpsretweets.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(["text", "user_location"])
	writer.writerows(outtweets)
	
	pass
