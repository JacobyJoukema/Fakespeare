from Tokenizer import Tokenizer
from RNN import RNN
from Utils import *
import numpy as np

class Generator:
    __init__ (self, fileName):
        self.t = Tokenizer()
        self.wordToInd = t.getWordToInd()
        self.indexToWord = t.getIndToWord()
        self.model = RNN(t.getVocabSize())
        load(fileName, model)

    def generateSentence (self):
        newSent = [wordToInd["SENTENCE_START"]]
        while not newSent[-1] == wordToInd["SENTENCE_END"]:
            nextWordProbs = self.model.forwardPropagation(newSent)[0]
            sampled = self.wordToInd["UNKNOWN_TOKEN"]
            while sampled == self.wordToInd["UNKNOWN_TOKEN"]:
                samples = np.random.multinomial(1,nextWordProbs[-1])
                sampled = np.argmax(samples)
            newSent.append(sampled)
        sentence = [self.indexToWord[x] for x in newSent[1:-1]]
        return (postParse(sentence))

    def postParse (self, sentence):
        sentence[0].capitalize()
        out = sentence[0]
        for i in sentence[1:]:
            if i == "," or i == "." or i ==":" or i == ";":
                out += i
            else:
                out += " " + i
        return out

for i in range (10):
    print ("Generating Sentence " + str(i))
    print (generateSentence(model, wordToInd, indexToWord))
