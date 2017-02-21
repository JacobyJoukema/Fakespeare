from twitter import *
from time import sleep
from Generator import Generator

def tweet (quote):
    accessToken = "778726628079742976-HAq2wk6WQxIE0XlbMBBJi9tEcpyjoeb"
    accessTokenS = "1M1cH5jyGQrm99WWfrQWw8tfmmQnxAvX7m1IN14w0H5AT"
    consumerKey = "Kitw7q1GVZj93vN1CPZwrUdUc"
    consumerS = "b19uuiJ6ey1DopmXqiNdI3ZR36W8DtscjN7LVCKZym06Bu5awh"

    t = Twitter (auth=OAuth(accessToken, accessTokenS, consumerKey, consumerS))

    t.statuses.update(status=quote)


if __name__ == '__main__':
    gen = Generator("Data/FakespeareProg.npz")
    while True:
        print ("Curating")
        num, sentence = gen.curateSentence()
        for i in range (num):
            print ("Tweeting: " + str(sentence[i]))
            tweet (sentence[i])
        sleep (9*60*60)
