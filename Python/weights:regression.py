import numpy as np
def weight(X,y):
 w=np.linalg.inv(X.T@X)@X.T@y
 return w   
X=np.array([[1,1],[1,3],[1,4]])
y=np.array([[2],[5],[6]])
w=weight(X,y)

x_n=np.array([[1,5]])
y_n=x_n@w