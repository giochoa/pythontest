import tweepy

auth = tweepy.OAuthHandler('KINHgXqoSTS5ReyTnjXSYAA6w', 'ehCnMc37yfAf6PPdmzQMJM7pkUb5HYsnPfZw0vf5m9rxPNEbVm')
auth.set_access_token('1488729367346040833-mQJ2oNZDK0Rj49uLojV9WAYL4oURe0', '8zzRNCJ9sGxcnxJxgVEQkfNC7kWL12Akgpd2gdUt6REo3')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)