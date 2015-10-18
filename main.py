import tweepy
import random
from nltk.tag import pos_tag
from GoogleSuggest import GoogleSuggest
import time

class TwitterAPI:
    def __init__(self):
        consumerKey = "ai3qktfWT8PgavFOMxX9byifZ"
        consumerSecret = "8PnQA3POB9ApqnoKncy08XPcFW7lpCNCLiK12sFiIvsyEIAyaq"
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        accessToken = "3835110802-mXI3pslqOAqpqLc0uNP402B8VOEyztcqzB3FVmZ"
        accessTokenSecret = "OnpyRnWS36fWVHByO2aVcQ88xsj5NaaDSHgNk4s3NPYdP"
        auth.set_access_token(accessToken, accessTokenSecret)
        self.api = tweepy.API(auth)

    def tweet(self, message, tweetID):
        print message
        print tweetID
        self.api.update_status(status = message, in_reply_to_status_id = tweetID)
        
    def getRandomRamesyLastTweet(self):
        tweets = self.api.user_timeline("@ra");
        return tweets[random.randint(0, len(tweets) - 1)];

if __name__ == "__main__":
    previousTweetIDs = []
    twitter = TwitterAPI()
    while True:
		try:
			tweet = twitter.getRandomRamesyLastTweet()
			tweetID = str(tweet.id)
			if not tweetID in previousTweetIDs:
				previousTweetIDs.append(tweetID)
				taggedTweet = pos_tag(tweet.text.split())
				propernouns = [word for word,pos in taggedTweet if ('NN' in pos or len(word) > 5) and not "@" in word and not 'RT' in word and not ":" in word]
				if len(propernouns) > 0:
					noun = propernouns[random.randint(0, len(propernouns) - 1)]
					suggestions = GoogleSuggest(noun).read()
					longSent = []
					for suggest in suggestions:
						if(' ' in suggest):
							longSent.append(suggest)
					if len(longSent) > 0:
						twitter.tweet('@ra ' + longSent[random.randint(0, len(longSent) - 1)], tweetID)
						time.sleep((30 + random.randrange(0, 30)) * 60)
		except:
			print "Error Happened!!!!"