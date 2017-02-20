#Ref

import numpy as np

def softmax (x):
    xt = np.exp(x-np.max(x))
    return xt/np.sum(xt)

def save (out, model):
    U, V, W = model.getValues()
    np.savez(out, U=U, V=V, W=W)
    print ("Saved network to: " + out)

def load (inp, model):
    npzfile = np.load(inp)
    U, V, W = npzfile["U"], npzfile["V"], npzfile["W"]
    model.hidden = U.shape[0]
    model.vocab = U.shape[1]
    model.setValues(U, V, W)

    print ("Successfully loaded: " + inp)
