import nltk
import numpy as np
import itertools

class Tokenizer:
    senStart = "SENTENCE_START"
    senEnd = "SENTENCE_END"
    unknown = "UNKNOWN_TOKEN"

    xTrain = []
    yTrain = []

    def __init__ (self, vocabSize=15000):
        self.vocabSize = vocabSize
        f = open('Data/Lines.txt', 'r')
        text = f.read()
        lines = text.split("--------------")

        lines = [line.replace('\n', ' ') for line in lines]
        #print (lines)
        sentences = [nltk.sent_tokenize(line.lower()) for line in lines]
        #['Doth u swag?']
        sentences = ["%s %s %s" % (self.senStart,sentence[0], self.senEnd) for sentence in sentences]
        #['SENTENCE_START', ['Doth', 'u', 'swag', '?'], 'SENTENCE_END']
        tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]

        #Ref
        wordFreq = nltk.FreqDist(itertools.chain(*tokenized))
        vocab = wordFreq.most_common(self.vocabSize-1)
        indexToWord = [x[0] for x in vocab]
        indexToWord.append(self.unknown)
        wordToInd = dict([(w,i) for i,w in enumerate(indexToWord)])

        for i, sent in enumerate(tokenized):
            tokenized[i] = [w if w in wordToInd else self.unknown for w in sent]

        #Ref
        self.xTrain = np.asarray([[wordToInd[word] for word in sent[:-1]] for sent in tokenized])
        self.yTrain = np.asarray([[wordToInd[word] for word in sent[1:]] for sent in tokenized])

        #print (tokenized)
    def getData (self):
        return self.xTrain, self.yTrain

    def getVocabSize (self):
        return self.vocabSize
T = Tokenizer()
