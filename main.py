__author__ = 'jot2102'
import tweepy
from random import shuffle
import string
class TweetText:
    'this is the sorted body of a tweet'

    def __init__(self, body):
        self.hash_tags = TweetText.get_hashtags(body)
        self.text_list = TweetText.get_text(body)

    def get_hashtags(body):
        hashtags= []
        split_body= body.split()
        for word in split_body:
            if word.startswith("#"):
                hashtags.append(word)
        return hashtags

    def get_text(body):
        text_list = []
        split_body=body.split()
        for word in split_body:
            if not any(i in word for i in '@/#'):
                text_list.append(word)
        return text_list




class Poem:
    'this is the generic poem class'
    poemcount= 0

    def __init__(self, name,body, taken_from,):

        self.name = name
        self.body = body
        self.taken_from = taken_from
        Poem.poemcount += 1
        self.number = Poem.poemcount

    def display_poem(self):
        print("The Poem is Called:" + self.name + "Reading" + self.body)

def first_poem(tweets):
    plist=[]
    for tweet in tweets:
        tweet_stuff = TweetText(tweet.text)
        plist =plist + tweet_stuff.text_list
    shuffle(plist)
    print(plist)




if __name__ == "__main__":

    consumer_key = 'SRGWO9unhMYWWCEaEL5Wr0jT0'
    consumer_secret = 'zdpasZZTaix3qEZ1lQ2Hd6AJSCHGcEKqulAvrL9pL924L2zT4M'
    access_token = '472550556-HSWBRpN4ppz3Tp6hOb8fg6d63N6ux4ZJ7OpgiuQN'
    access_token_secret = 'dLlwMXdUFbcbpRgRjIjlfjjzeKRWzR7fsJjTBoXhfhWZD'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    first_poem(public_tweets)
