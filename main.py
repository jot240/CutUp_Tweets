__author__ = 'jot2102'
import tweepy
from random import shuffle
import string


class TweetText:
    'this is the sorted body of a tweet'

    def __init__(self, body):
        self.hash_tags = TweetText.get_hashtags(body)
        self.text_list = TweetText.get_text(body)
        self.lines_list = TweetText.get_lines(body)

    def get_hashtags(body):
        hashtags = []
        split_body = body.split()
        for word in split_body:
            if word.startswith("#"):
                hashtags.append(word)
        return hashtags

    def get_text(body):
        text_list = []
        split_body = body.split()
        for word in split_body:
            if not any(i in word for i in '@/#'):
                word = word + ' '
                text_list.append(word)
        return text_list

    def get_lines(body):
        line_list = []

        split_lines = body.split('.!?')
        for line in split_lines:
            temp = TweetText.get_text(line)
            line = ''.join(temp)
            line_list.append(line)
        return line_list


class Poem:
    'this is the generic poem class'
    poemcount = 0

    def __init__(self, name, body, taken_from, ):
        self.name = name
        self.body = body
        self.taken_from = taken_from
        Poem.poemcount += 1
        self.number = Poem.poemcount

    def display_poem(self):
        print("The Poem is Called:" + self.name + "Reading" + self.body)


def first_poem(tweets):
    plist = []
    plist2= []
    pfile = open('C:\Python34\CutUp_Tweets\poem1.txt', 'w')
    pfile2 = open('C:\Python34\CutUp_Tweets\poem2.txt', 'w')
    for tweet in tweets:
        tweet_stuff = TweetText(tweet.text)
        plist = plist + tweet_stuff.text_list
        plist2 = plist2 +tweet_stuff.lines_list
    shuffle(plist)
    shuffle(plist2)
    print(plist)
    print(plist2)
    for i in range(0, len(plist)):
        if any(j in plist[i] for j in '.,?!'):
            plist.insert(i + 1, '\n')
    for i in range(0,len(plist2)):
        plist2.insert(i+1, '\n')
    for item in plist:
        pfile.write(item)
    # for item2 in plist2:
    #     pfile2.write(item2)


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
