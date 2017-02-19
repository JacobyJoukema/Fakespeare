from RNN import RNN
from Tokenizer import Tokenizer
import numpy as np

def testSystem ():
    t = Tokenizer()

    xTrain, yTrain = t.getData()
    np.random.seed(10)
    model = RNN(15000)
    o, s = model.forwardPropagation(xTrain[30])
    predictions = model.predict(xTrain[30])
    print (o.shape)
    print (o)
    print (predictions.shape)
    print (predictions)

    print ("Expected Loss: \n" + str(np.log(model.vocab)))
    print ("Actual Loss:")
    print (model.calculateLoss(xTrain[:100],yTrain[:100]))

def testGradient ():
    gradCheckSize = 100
    np.random.seed(10)
    CheckModel = RNN(gradCheckSize,10, bpttTrunc=1000)
    CheckModel.gradientCheck([0,1,2,3], [1,2,3,4])

testSystem ()
testGradient()
