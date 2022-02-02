import time
import tweepy

auth = tweepy.OAuthHandler('KINHgXqoSTS5ReyTnjXSYAA6w', 'ehCnMc37yfAf6PPdmzQMJM7pkUb5HYsnPfZw0vf5m9rxPNEbVm')
auth.set_access_token('1488729367346040833-mQJ2oNZDK0Rj49uLojV9WAYL4oURe0', '8zzRNCJ9sGxcnxJxgVEQkfNC7kWL12Akgpd2gdUt6REo3')

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
def limit_handle(cursor):
    try:
       while True:
         yield cursor.next()
    except tweepy.RateLimitError:
       time.sleep(1000)    

# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     if follower.name == '':
#         follower.follow()
#     print(follower.name)  

search_item = 'nasa'
numberOfTweets = 10

for tweet in tweepy.Cursor(api.search, search_item).items(numberOfTweets):
    try:
        tweet.favorite()
        print('likey')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break       