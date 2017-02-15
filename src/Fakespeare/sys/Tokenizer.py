import nltk
import numpy as np
import itertools

class Tokenizer:
    def __init__ (self):
        senStart = "SENTENCE_START"
        senEnd = "SENTENCE_END"
        unknown = "UNKNOWN_TOKEN"
        vocabSize = 15000

        f = open('Data/Lines.txt', 'r')
        text = f.read()
        lines = text.split("--------------")

        lines = [line.replace('\n', ' ') for line in lines]
        #print (lines)
        sentences = [nltk.sent_tokenize(line.lower()) for line in lines]
        #['Doth u swag?']
        sentences = ["%s %s %s" % (senStart,sentence[0], senEnd) for sentence in sentences]
        #['SENTENCE_START', ['Doth', 'u', 'swag', '?'], 'SENTENCE_END']
        tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]

        #Ref
        wordFreq = nltk.FreqDist(itertools.chain(*tokenized))
        vocab = wordFreq.most_common(vocabSize-1)
        indexToWord = [x[0] for x in vocab]
        indexToWord.append(unknown)
        wordToInd = dict([(w,i) for i,w in enumerate(indexToWord)])

        for i, sent in enumerate(tokenized):
            tokenized[i] = [w if w in wordToInd else unknown for w in sent]

        #Ref
        xTrain = np.asarray([[wordToInd[word] for word in sent[:-1]] for sent in tokenized])
        yTrain = np.asarray([[wordToInd[word] for word in sent[1:]] for sent in tokenized])

        print (tokenized)
    def getData (self):
        return xTrain, yTrain

T = Tokenizer()
