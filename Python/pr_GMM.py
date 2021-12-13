import numpy as np
def norma(s,mu,xo):
    N=(1/np.sqrt(2*np.pi*s**2))*np.exp(-np.power(xo-mu,2)/(2*s**2))
    return N
def pro(mus,sigs,w,n,xo):
    ab=w[n-1]*norma(sigs[n-1],mus[n-1],xo)
    be=0
    for i in range(len(w)):
        bei=w[i]*norma(sigs[i],mus[i],xo)
        be+=bei
    pr=ab/be
    return pr

mus=[18.347,14.997,18.421]
sigs=[1.2193,0.986,1.1354]
w=[.13,.55,.32]

print(pro(mus,sigs,w,2,15.38))