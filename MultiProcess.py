# import multiprocessing
# from random import randint
#
# def HH(name):
#     print("in the multiprecess ", name)
#
#
#
# if __name__ == "__main__":
#     process = []
#     for i in range(10):
#         process.append(multiprocessing.Process(target=HH, args=(str(randint(10, 200)),)))
#     for j in process:
#         j.start()
#         j.join()
#
#     print('Done')

# --------------------------------------------
# import tweepy
# consumer_key = 'ROtFC95DDvZMUSAJ'
# consumer_secret = '0HM1SBdSw4aMhSUEj9QNpzwwXSjKZn'
# key = '7640276498WdYUUCV'
# secret = 'K59rz3ECGP8no9jPwvPbRZAYJkrqG'
#
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(key, secret)
# b = auth.get_username()
# api = tweepy.API(auth)
# media = api.media_upload(r"F:\AISA_TheVirtualFriend\screenshot.png")
# tweet = "Great scifi author or greatest scifi author? #williamgibson"
# post_result = api.update_status(status=tweet, media_ids=[media.media_id])
# -------------------------------------------

# import pandas as pd
#
# data =pd.read_csv("credential.csv")
# print(list(data["consumer_key"]))
# print(list(data["consumer_secret"]))
# print(list(data["secret"]))
# print(list(data["key"]))

# --------------------------------------------

f = open("TweetMessage.txt", 'r')
a = f.readlines()
print(a)

