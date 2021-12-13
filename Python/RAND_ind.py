import numpy as np

def S_ind(Mat):
    n=Mat.shape[0]*Mat.shape[0]
    s=0
    for i in range(n):
       si=Mat.item(i)*(Mat.item(i)-1)/2
       s+=si
    return(s)

def D_ind(Mat):
    N=Mat.sum()
    d1=N*(N-1)/2
    nz=Mat.sum(0)
    for n1 in nz:
        d1-=n1*(n1-1)/2
    nq=Mat.sum(1)
    for n2 in nq:
        d1-=n2*(n2-1)/2
    d=d1+S_ind(Mat)
    return(d)

Mat=np.array([[114,0,32],[0,119,0],[8,0,60]])
S=S_ind(Mat)
D=D_ind(Mat)
N=Mat.sum()
R=(S+D)/(.5*N*(N-1))