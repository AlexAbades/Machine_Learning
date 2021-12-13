#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[19]:


import numpy as np
from math import log2


# ### Class Error

# In[12]:


def p(v):
    "v: branch"
    return v/np.sum(v)


# In[20]:


def class_error(v):
    return 1 - max(p(v))

def Gini(v):
    return 1 - np.sum(p(v)**2)

def Entropy(v):
    return - np.sum(p(v)*log2(p(v)))


# In[22]:


def impurity(root,v1,v2,fun):
    "fun can be: class_error, Gini, Entropy"
    I_r = fun(root)
    I_v1 = fun(v1)
    I_v2 = fun(v2)
    
    return I_r - np.sum(v1)/np.sum(root)*I_v1 - np.sum(v2)/np.sum(root)*I_v2


# In[24]:


root = [5,10]
v1 = [1,4]
v2 = [4,6]

I = impurity(root,v1,v2,Gini)
print(i)


# In[ ]:





# In[4]:


root = [17, 15]
split1 = [13, 2]
split2 = [4, 13]

parent = 1 - np.max(root)/np.sum(root)
child1 = (np.sum(split1)/np.sum(root))*(1 - (np.max(split1)/np.sum(split1)))
child2 = (np.sum(split2)/np.sum(root))*(1 - (np.max(split2)/np.sum(split2)))

gain = parent - child1 - child2

print(gain)


# In[3]:


root = [100, 100]
split1 = [45, 1]
split2 = [47, 66]
split3 = [8, 33]

parent = 1 - (np.max(root)/np.sum(root))
child1 = (np.sum(split1)/np.sum(root))*(1 - (np.max(split1)/np.sum(split1)))
child2 = (np.sum(split2)/np.sum(root))*(1 - (np.max(split2)/np.sum(split2)))
child3 = (np.sum(split3)/np.sum(root))*(1 - (np.max(split3)/np.sum(split3)))

gain = parent - child1 - child2 - child3

print(gain)


# **Comment:** Select the Split with the biggest gain

# In[4]:


root = [70, 70, 70]
split1 = [24, 70 , 0]
split2 = [46, 0, 70]

parent = 1 - (np.max(root)/np.sum(root))
child1 = (np.sum(split1)/np.sum(root))*(1 - (np.max(split1)/np.sum(split1)))
child2 = (np.sum(split2)/np.sum(root))*(1 - (np.max(split2)/np.sum(split2)))

gain = parent - child1 - child2

print(gain)


# ### Gini

# In[5]:


root = [18, 18, 18]
split1 = [6, 9 , 3]
split2 = [4, 6, 10]
split3 = [8, 3, 5]

parent, child1, child2, child3 = 1, 1, 1, 1

for i in range(len(whole)):
    parent = parent - np.power(root[i]/np.sum(root), 2)
    child1 = child1 - np.power(split1[i]/np.sum(split1), 2)
    child2 = child2 - np.power(split2[i]/np.sum(split2), 2)
    child3 = child3 - np.power(split3[i]/np.sum(split3), 2)

child1 = child1*np.sum(split1)/np.sum(root)
child2 = child2*np.sum(split2)/np.sum(root)
child3 = child3*np.sum(split3)/np.sum(root)

gain = parent - child1 - child2 - child3

print(gain)

