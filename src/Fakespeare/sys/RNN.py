import numpy as np
from Utils import *
import Tokenizer

class RNN:
    def __init__ (self, vocab, hidden=100, bptt=4):
        self.vocab = vocab
        self.hidden = hidden
        self.bptt = bptt

        #Ref
        self.U = np.random.uniform(-np.sqrt(1./vocab), np.sqrt(1./vocab), (hidden, vocab))
        self.V = np.random.uniform(-np.sqrt(1./hidden), np.sqrt(1./hidden), (vocab, hidden))
        self.W = np.random.uniform(-np.sqrt(1./hidden), np.sqrt(1./hidden), (hidden, hidden))

    def forwardPropagation (self, x):
        #Time Steps
        T = len(x)

        s = np.zeroes ((T+1, self.hidden))
        s[-1] = np.zeroes(self.hidden)

        o = np.zeroes ((T, self.vocab))

        for t in np.arrange(T):
            s[t] = np.tanh(self.U[:,x[t]] + self.W.dot(s[t-1]))
            o[t] = softmax(self.V.dot(s[t]))

        return [o,s]
    RNN.forwardPropagation = forwardPropagation

    def predict (self, x):
        o, s = self.forwardPropagation(x)
        return np.argmax(o,axis=1)
    RNN.predict = predict




t = Tokenizer()

xTrain, yTrain = t.getData()
np.random.seed(10)
model = RNN(1000)
o, s = model.forwardPropagation(xTrain[10])
print (o.shape)
print (o)
