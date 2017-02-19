from RNN import RNN
from Tokenizer import Tokenizer
import numpy as np
import time
from datetime import datetime
import sys
from Utils import *

def trainWithSGD (model, xTrain, yTrain, learningRate=.005, cycles=100, evalAfterLoss = 5):
    losses = []
    examplesSeen = 0
    for cycle in range (cycles):
        if (cycle % evalAfterLoss == 0):
            loss = model.calculateLoss(xTrain,yTrain)
            losses.append((examplesSeen, loss))
            time = datetime.now().strftime('%y-%m-%d %H:%M:%S')
            print (str (time) + ": Loss after, Examples: " + str(examplesSeen) + " Cycle: " + str(cycle) + " Loss: " + str(loss))

            if (len(losses) > 1 and losses[-1][1] > losses [-2][1]):
                learningRate = learningRate*.5
                print ("New Learning Rate: " + str (learningRate))
            sys.stdout.flush()
        for i in range (len (yTrain)):
            model.sgdStep(xTrain[i], yTrain[i], learningRate)
            examplesSeen+=1

def testTrain ():
    print ("Starting Test")
    np.random.seed(10)
    print ("Starting Tokenization")
    t = Tokenizer(vocabSize=15000)
    print ("Tokenizer Complete")
    vocabSize = t.getVocabSize()
    print ("Vocab Size: " + str(vocabSize))
    xTrain, yTrain = t.getData()

    print ("Constructing Model")
    model = RNN(vocabSize)
    print ("Starting Timer")
    start = time.clock()
    model.sgdStep(xTrain[10], yTrain[10], .005)
    end = time.clock()
    print ("One Step Time: " + str(end-start))

    print ("Starting Training")
    losses = trainWithSGD(model,xTrain[:100], yTrain[:100], cycles=10, evalAfterLoss=1)
    Utils.save("Data/TestModel.npz", model)

testTrain()
