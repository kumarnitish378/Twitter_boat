import multiprocessing as mlt
import tweepy
from time import sleep, time
from pandas import read_csv
from random import randint


print("Loading credential File...")
data = read_csv('credential.csv')
print("reading Done!")

class twit():
    def go(self,name):
        print("in the class", name)

    def bot(self, consumer_key, consumer_secret, key,secret, message, numbere_of_msg):
        consumer_key = consumer_key
        consumer_secret = consumer_secret

        key = key
        secret = secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        b = auth.get_username()
        api = tweepy.API(auth)
        tweet = message
        n = int(numbere_of_msg)
        c = 0
        for i in range(n):
            api = tweepy.API(auth)
            try:
                api.update_status(tweet + " " + str(time()))
                print("send {}".format(i + 1))
                sleep(0.5)
                c += 1
            except Exception as eroor:
                print(eroor)
                pass
        print("succesfull send = {}".format(c))


    def findTag(self, consumer_key, consumer_secret, key,secret, Tag, date_since, items):
        consumer_key = consumer_key
        consumer_secret = consumer_secret

        key = key
        secret = secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        b = auth.get_username()
        api = tweepy.API(auth)
        search_words = Tag
        n = int(items)
        tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since).items(n)

        for tw in tweets:
            print(tw.text)

    def postWithImage(self, consumer_key, consumer_secret, key,secret, message, numbere_of_msg, file_name):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(key, secret)
        b = auth.get_username()
        api = tweepy.API(auth)
        # media = api.media_upload(r"F:\AISA_TheVirtualFriend\screenshot.png")
        media = api.media_upload(file_name)
        tweet = message
        for tw in range(numbere_of_msg):
            api.update_status(status=tweet, media_ids=[media.media_i])
            print("Send Done!")
            sleep(0.5)
        post_result = api.update_status(status=tweet, media_ids=[media.media_id])



if __name__ == "__main__":
    obj = []
    number_of_Bot = len(data)
    number_of_msg = 20
    # Creating Bot Object
    for i in range(number_of_Bot):
        obj.append(twit())

    consumer_key = list(data["consumer_key"])
    consumer_secret = list(data["consumer_secret"])
    key = list(data["key"])
    secret = list(data["secret"])

    # Creating objects for multiple tweets only Text tweet
    message = "The real reason behind #RCB is Comeback"+ str(time())
    read = open("TweetMessage.txt")
    message = read.readlines()
    if message is None:
        message["Hello To all"] 
    for j in range(number_of_Bot):
        obj[j].bot(consumer_key[j], consumer_secret[j], key[j], secret[j], message[randint(0, len(message))], number_of_msg)
    # Creating Multiple Process Parallel
    process = []
    for i in range(number_of_Bot):
        process.append(mlt.Process(target=obj[i].bot, args=(consumer_key[i], consumer_secret[i], key[i], secret[i], message[randint(0, len(message))], number_of_msg),))

    # start process
    for j in process:
        j.start()
        # j.join()
    # ---------------------------multiple Tweet with image File---------------
    a = 2
    if a == 1:
        image_caption = "I like this Post #JivaSport "+str(time())
        num_of_post = 5
        post_object = []
        for post in range(number_of_Bot):
            post_object.append(twit())
        path = "F:\AISA_TheVirtualFriend\screenshot.png"
        for jj in range(number_of_Bot):
            post_object[jj].postWithImage(consumer_key[jj], consumer_secret[jj], key[jj], secret[jj], message[randint(0, len(message))], number_of_msg, path)

    #     Creating Process for Image Post
        imag_process = []
        for kk in range(number_of_Bot):
            imag_process.append(mlt.Process(target=post_object[kk].postWithImage, args=(consumer_key[jj], consumer_secret[jj], key[jj], secret[jj], message[randint(0, len(message))], number_of_msg, path),))

        for ram in imag_process:
            ram.start()
        print("All process Done!")

    print('Done')