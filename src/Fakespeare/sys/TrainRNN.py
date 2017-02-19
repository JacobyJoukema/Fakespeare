from RNN import RNN
from Tokenizer import Tokenizer
import numpy as np
import timeit

def trainWithSDG (model, xTrain, yTrain, learningRate=.005, cycles=100, evalAfterLoss = 5):
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
            model.sdgStep(xTrain, yTrain, learningRate)
            examplesSeen+=1

t = Tokenizer()
vocabSize = t.getVocabSize()
xTrain, yTrain = t.getData()

model = RNN(vocabSize)

model.sdgStep(xTrain[10], yTrain[10], .005)
