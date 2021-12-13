import numpy as np
def sigmoid(x,w):
    z=x.T@w
    sig=1/(1+np.exp(-z))
    return sig
x=np.array([1,16])
w=np.array([418.94,-26.12])

print(sigmoid(x.T,w))
