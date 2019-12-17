import re
import tweepy                                                    #install using pip
from tweepy import OAuthHandler                                  #install using pip
from textblob import TextBlob                                    #install using pip

class TwitterClient(object):
    def __init__(self):
    
    #In order to fetch tweets through Twitter API, one needs to register an App through their twitter account.
    #Open this link and click the button: ‘Create New App’
    #Fill the application details. You can leave the callback url field empty.
    #Once the app is created, you will be redirected to the app page.
    #Open the ‘Keys and Access Tokens’ tab.
    #Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.
    
        consumer_key = "xxxxxxxxxxxxxx"
        consumer_secret = "xxxxxxxxxxxxxxxxxxx"
        access_token = "xxxxxxxxxxxxxxxx"
        access_token_secret = "xxxxxxxxxxxxx"
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
    def clean_tweet(self, tweet):                                     # To remove special characters punctuations etc.
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\ / \ / \S+)", " ", tweet).split())
    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    def get_tweets(self, query, count = 100000):
        tweets = []
        try:
            fetched_tweets = self.api.search(q = query , count = count)
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet["text"] = tweet.text
                parsed_tweet["sentiment"] = self.get_tweet_sentiment(tweet.text)
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error: " + str(e))
def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = "London", count = 1000000)               # query and count can be whatever you like
    ptweets = [tweet for tweet in tweets if tweet["sentiment"] == "positive"]
    print("Positive tweet percentage: {} %".format(100*len(ptweets)/len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet["sentiment"] == "negative"]
    print("Negative tweet percentage: {} %".format(100*len(ntweets)/len(tweets)))
    print("Neutral tweet percentage: {} %".format(100*(len(tweets) - len(ntweets) + len(ptweets))/len(tweets)))
    print("\n Positive Tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
    print("\nNegative Tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
if __name__ == "__main__":
    main()
