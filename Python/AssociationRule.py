#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np
from apyori import apriori


# ### Functions

# In[2]:


def mat2transactions(X, labels=[]):
    T = []
    for i in range(X.shape[0]):
        l = np.nonzero(X[i, :])[0].tolist()
        if labels:
            l = [labels[i] for i in l]
        T.append(l)
    return T

def print_apriori_rules(rules):
    frules = []
    for r in rules:
        for o in r.ordered_statistics:        
            conf = o.confidence
            supp = r.support
            x = ", ".join( list( o.items_base ) )
            y = ", ".join( list( o.items_add ) )
            print("{%s} -> {%s}  (supp: %.3f, conf: %.3f)"%(x,y, supp, conf))
            frules.append( (x,y) )
    return frules


# ### Support

# In[3]:


Xbin = [[0, 1, 1, 0, 1], 
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0]]

Xbin = np.asarray(Xbin)

attributeNamesBin = ['f1', 'f2', 'f3', 'f4', 'f5']

T = mat2transactions(Xbin,labels=attributeNamesBin)
rules = apriori(T, min_support=0.01)
print_apriori_rules(rules)


# **Comment:** To find confidence search "{f1, f4} -> {f5}"

# In[4]:


Xbin = [[1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1]]

Xbin = np.asarray(Xbin)

attributeNamesBin = ['x1', 'x2', 'x3', 'x4', 'x5']

T = mat2transactions(Xbin,labels=attributeNamesBin)
rules = apriori(T, min_support=0.4)
print_apriori_rules(rules)

