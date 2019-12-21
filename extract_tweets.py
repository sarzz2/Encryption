import tweepy

consumer_key = "xxxxxxxxxx"                   
consumer_secret = "xxxxxxxx"
access_token = "xxxxxxxxx"
access_token_secret = "xxxxxxxxxx"
def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    number = 200
    tweets = api.user_timeline(screen_name = username)
    tmp = []
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    for i in tmp:
        print(i)

if __name__ == "__main__":
    get_tweets("daviddobrik")
