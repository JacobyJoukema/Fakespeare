import numpy as np
from Utils import *
from Tokenizer import Tokenizer
import operator

class RNN:
    def __init__ (self, vocab, hidden=100, bpttTrunc=4):
        self.vocab = vocab
        self.hidden = hidden
        self.bpttTrunc = bpttTrunc

        #Ref
        self.U = np.random.uniform(-np.sqrt(1./self.vocab), np.sqrt(1./self.vocab), (self.hidden, self.vocab))
        self.V = np.random.uniform(-np.sqrt(1./self.hidden), np.sqrt(1./self.hidden), (self.vocab, self.hidden))
        self.W = np.random.uniform(-np.sqrt(1./self.hidden), np.sqrt(1./self.hidden), (self.hidden, self.hidden))

    def forwardPropagation (self, x):
        #Time Steps
        T = len(x)

        s = np.zeros ((T+1, self.hidden))
        s[-1] = np.zeros(self.hidden)

        o = np.zeros ((T, self.vocab))

        for t in np.arange(T):
            print (self.U.shape)
            print (self.W.shape)
            s[t] = np.tanh(self.U[:,x[t]] + self.W.dot(s[t-1]))
            o[t] = softmax(self.V.dot(s[t]))

        return [o,s]
    #RNN.forwardPropagation = forwardPropagation

    def predict (self, x):
        o, s = self.forwardPropagation(x)
        return np.argmax(o,axis=1)
    #RNN.predict = predict

    def calculateTotalLoss (self, x , y):
        L = 0
        for i in np.arange(len(y)):
            o,s = self.forwardPropagation(x[i])
            correctPredictions = o[np.arange(len(y[i])),y[i]]
            L+= -1*np.sum(np.log(correctPredictions))
        return L

    def calculateLoss(self, x,y):
        N = np.sum((len(y_i) for y_i in y))
        return self.calculateTotalLoss(x,y)/N

    def bptt (self, x, y):
        T = len(y)
        o, s = self.forwardPropagation(x)
        dLdU = np.zeros(self.U.shape)
        dLdV = np.zeros(self.V.shape)
        dLdW = np.zeros(self.W.shape)
        deltaO = o
        deltaO[np.arange(len(y)),y]-=1.
        for t in np.arange(T)[::-1]:
            dLdV += np.outer(deltaO[t],s[t].T)
            deltaT = self.V.T.dot(deltaO[t])*(1-(s[t]**2))
            for bpttStep in np.arange(max(0,t-self.bpttTrunc),t+1)[::-1]:
                dLdW+=np.outer(deltaT,s[bpttStep-1])
                dLdU[:,x[bpttStep]] += deltaT
                deltaT = self.W.T.dot(deltaT)*(1-s[bpttStep-1]**2)
        return [dLdU, dLdV, dLdW]

    def gradientCheck (self, x, y, h =0.001, thresh = 0.01):
        bpttGrad = self.bptt(x,y)
        modelParams = ['U','V','W']
        for pidx, pname in enumerate(modelParams):
            param = operator.attrgetter(pname)(self)
            print ("Gradient Check for Parameter " + pname + " and size " + str (np.prod(param.shape)))
            it = np.nditer(param, flags=['multi_index'], op_flags=['readwrite'])
            while not it.finished:
                ix = it.multi_index
                original = param[ix]
                param[ix] = original + h
                gradPlus = self.calculateTotalLoss([x],[y])
                param[ix] = original - h
                gradMinus = self.calculateTotalLoss([x],[y])
                estGrad = (gradPlus- gradMinus)/(2*h)
                param[ix] = original

                backpropGrad = bpttGrad[pidx][ix]
                relativeErr = np.abs(backpropGrad - estGrad)/(np.abs(backpropGrad) + np.abs(estGrad))
                if relativeErr >= thresh:
                    print ("Gradient Err: Param " + pname + "ix " + str(ix))
                    print ("+h loss " + str(gradPlus))
                    print ("-h loss " + str(gradMinus))
                    print ("Est Grad " + str (estGrad))
                    print ("BackProp Grad" + str(backpropGrad))
                    print ("RelativeErr" + str(relativeErr))
                    return
                it.iternext()
            print ("PASS: Gradient Check for Parameter " + pname)

    def sgdStep (self, x, y, learningRate):
        dLdU, dLdV, dLdW = self.bptt(x,y)

        self.U -= learningRate*dLdU
        self.V -= learningRate*dLdV
        self.W -= learningRate*dLdW
