from twitter import *
from Tokenizer import Tokenizer
from RNN import RNN
from Utils import *
import numpy as np

def tweet (quote):
    accessToken = "778726628079742976-HAq2wk6WQxIE0XlbMBBJi9tEcpyjoeb"
    accessTokenS = "1M1cH5jyGQrm99WWfrQWw8tfmmQnxAvX7m1IN14w0H5AT"
    consumerKey = "Kitw7q1GVZj93vN1CPZwrUdUc"
    consumerS = "b19uuiJ6ey1DopmXqiNdI3ZR36W8DtscjN7LVCKZym06Bu5awh"

    t = Twitter (auth=OAuth(accessToken, accessTokenS, consumerKey, consumerS))

    t.statuses.update(status=quote)

def generateSentence (model, wordToInd, indexToWord):
    newSent = [wordToInd["SENTENCE_START"]]
    while not newSent[-1] == wordToInd["SENTENCE_END"]:
        nextWordProbs = model.forwardPropagation(newSent)[0]
        sampled = wordToInd["UNKNOWN_TOKEN"]
        while sampled == wordToInd["UNKNOWN_TOKEN"]:
            samples = np.random.multinomial(1,nextWordProbs[-1])
            sampled = np.argmax(samples)
        newSent.append(sampled)
    sentence = [indexToWord[x] for x in newSent[1:-1]]
    return (" ".join(sentence))

if __name__ == '__main__':
    t = Tokenizer()
    wordToInd = t.getWordToInd()
    indexToWord = t.getIndToWord()
    model = RNN(t.getVocabSize())
    load("Data/TestModel.npz", model)
    for i in range (10):
        print ("Generating Sentence " + str(i))
        print (generateSentence(model, wordToInd, indexToWord))
