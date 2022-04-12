import tweepy
from time import sleep
from random import randint
consumer_key = 'Put your consumer_key'
consumer_secret = 'Put your consumer_secret'

# key = 'Put your Key'
secret = 'Put your secret Key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
b = auth.get_username()
print(b)
api = tweepy.API(auth)
tweet = str(input("enter message: "))
n = int(input("How many time want to tweet? = "))
c = 0
for i in range (n):
    api = tweepy.API(auth)
    try:
        a = api.update_status(tweet + " " + str(i+5/2+1.07 + randint(10,1000)))
        print(a)
        print("send {}".format(i+1))
        sleep(1)
        c += 1
    except:
        pass
print("succesfull send = {}".format(c))
