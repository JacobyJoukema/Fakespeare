from Tokenizer import Tokenizer
from RNN import RNN
from Utils import *
import numpy as np

class Generator:
    def __init__ (self, fileName):
        t = Tokenizer()
        self.wordToInd = t.getWordToInd()
        self.indexToWord = t.getIndToWord()
        self.model = RNN(t.getVocabSize())
        load(fileName, self.model)

    def postParse (self, sentence):
        sentence = [v for v in sentence if not v == "[" or v == "]"]
        out = str(sentence[0][0].upper()+sentence[0][1:])
        for i in sentence[1:]:
            if i == "," or i == "." or i ==":" or i == ";" or i=="?" or i=="!":
                out += i
            elif i=="i":
                out+= " I"
            else:
                out += " " + i
        return out

    def generateSentence (self):
        newSent = [self.wordToInd["SENTENCE_START"]]
        while not newSent[-1] == self.wordToInd["SENTENCE_END"]:
            nextWordProbs = self.model.forwardPropagation(newSent)[0]
            sampled = self.wordToInd["UNKNOWN_TOKEN"]
            while sampled == self.wordToInd["UNKNOWN_TOKEN"]:
                samples = np.random.multinomial(1,nextWordProbs[-1])
                sampled = np.argmax(samples)
            newSent.append(sampled)
        sentence = [self.indexToWord[x] for x in newSent[1:-1]]
        #print (sentence)
        return (self.postParse(sentence))

g = Generator("Data/FakespeareProg.npz")
for i in range (10):
    print ("Generating Sentence " + str(i))
    sent = g.generateSentence()
    print ("Sentence Length: " + str (len(sent)))
    print (sent)