from twitter import *
from time import sleep
from Generator import Generator

def tweet (quote):
    f = open("Data/cred.txt", "r")
    creds = f.read()
    creds = creds.split(",")
    accessToken = creds[0]
    accessTokenS = creds[1]
    consumerKey = creds[2]
    consumerS = creds[3]

    t = Twitter (auth=OAuth(accessToken, accessTokenS, consumerKey, consumerS))

    t.statuses.update(status=quote)


if __name__ == '__main__':
    gen = Generator("Data/FakespeareProg.npz")
    while True:
        print ("Curating")
        num, sentence = gen.curateSentence()
        for i in range (num):
            print ("Tweeting: " + str(sentence[i]))
            tweeted = False
            while not tweeted:
                try:
                    tweet (sentence[i])
                    tweeted = True
                except:
                    print ("Retry")
        sleep (9*60*60)
