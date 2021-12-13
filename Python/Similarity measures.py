#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np


# In[2]:


def similarity(X, Y, method):
    '''
    method   string defining one of the following similarity measure
           'SMC', 'smc'             : Simple Matching Coefficient
           'Jaccard', 'jac'         : Jaccard coefficient 
           'ExtendedJaccard', 'ext' : The Extended Jaccard coefficient
           'Cosine', 'cos'          : Cosine Similarity
           'Correlation', 'cor'     : Correlation coefficient
    '''
    X = np.mat(X)
    Y = np.mat(Y)
    N1, M = np.shape(X)
    N2, M = np.shape(Y)
    method = method[:3].lower()
    if method=='smc': # SMC
        X,Y = binarize(X,Y);
        sim = ((X*Y.T)+((1-X)*(1-Y).T))/M
    elif method=='jac': # Jaccard
        X,Y = binarize(X,Y);
        sim = (X*Y.T)/(M-(1-X)*(1-Y).T)        
    elif method=='ext': # Extended Jaccard
        XYt = X*Y.T
        sim = XYt / (np.log( np.exp(sum(np.power(X.T,2))).T * np.exp(sum(np.power(Y.T,2))) ) - XYt)
    elif method=='cos': # Cosine
        sim = (X*Y.T)/(np.sqrt(sum(np.power(X.T,2))).T * np.sqrt(sum(np.power(Y.T,2))))
    elif method=='cor': # Correlation
        X_ = zscore(np.asarray(X),axis=1,ddof=1) # Matrix type throws error
        Y_ = zscore(np.asarray(Y),axis=1,ddof=1)
        sim = (X_*Y_.T)/(M-1)
    return sim


# In[3]:


def binarize(X,Y=None):
    x_was_transposed = False
    if Y is None:
        if X.shape[0] == 1:
            x_was_transposed = True
            X = X.T;
        
        Xmedians = np.ones((np.shape(X)[0],1)) * np.median(X,0)
        Xflags = X>Xmedians
        X[Xflags] = 1; X[~Xflags] = 0
        if x_was_transposed:
            return X.T
        return X
    else:
        return [binarize(X,None),binarize(Y,None)]


# ### SMC 

# In[12]:


X = np.array([1, 1, 1, 1, 2, 2, 2, 1, 1, 2])
q = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])

sim = similarity(X, q, 'smc')
print(sim)


# ### Jaccard

# In[13]:


X = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
q = np.array([2, 2, 2, 2, 1, 1, 1, 2, 2, 1])

sim = similarity(X, q, 'jac')
print('Similarity results:\n {0}'.format(sim))


# ### Cosine

# In[6]:


X = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
q = np.array([2, 2, 2, 2, 1, 1, 1, 2, 2, 1])

sim = similarity(X, q, 'cos')
print('Similarity results:\n {0}'.format(sim))


# In[48]:


conf = [[114, 0, 32], [0, 119, 0], [8, 0, 60]]

S = 0
D = np.sum(conf)*(np.sum(conf)-1)/2

for i in range(len(conf)):
    D1 =  np.sum(conf[i])
    D2 = np.sum([row[i] for row in conf])
    D = D - (D1*(D1-1)/2) - (D2*(D2-1)/2)
    for j in range(len(conf)):
        S = S + (conf[i][j]*(conf[i][j]-1)/2)

D = D + S

Rzq = (S+D)/(np.sum(conf)*(np.sum(conf)-1)/2)
print(Rzq)


# In[47]:


Rzq


# In[43]:


np.sum(conf[2])


# In[24]:


conf.T


# In[1]:


import toolbox_extended as te  # pip install --ignore-installed ml02450
import toolbox_02450 as tb


# In[3]:


1.95 + 0.73


# In[4]:


2/2.6799999999999997


# In[ ]:




