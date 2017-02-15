import nltk

class Tokenizer:
    def __init__ (self):
        senStart = "SENTENCE_START"
        senEnd = "SENTENCE_END"

        f = open('Data/Lines.txt', 'r')
        text = f.read()
        lines = text.split("--------------")

        lines = [line.replace('\n', ' ') for line in lines]
        #print (lines)
        sentences = [nltk.sent_tokenize(line.lower()) for line in lines]
        sentences = ["%s %s %s" % (senStart,sentence, senEnd) for sentence in sentences]

        tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
        print (tokenized)

        #Ref
        xTrain = np.asarray([[wordToInd[word] for word in sent[:-1]] for sent in tokenized])
        yTrain = np.asarray([[wordToInd[word] for word in sent[1:]] for sent in tokenized])

        print (tokenized)
    def getData (self):
        return xTrain, yTrain

T = Tokenizer()
