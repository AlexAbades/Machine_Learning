#!/usr/bin/env python
# coding: utf-8

# ### Libaries

# In[1]:


import math
import numpy as np


# ### Softmax Function

# In[2]:


#Select a Point
x = [0, 1]
w = [[1, 1], [-1, -1], [1, -1]]

prob = []
for i in range(len(w)):
    prob.append(math.exp(np.matmul(w[i], x))/(math.exp(np.matmul(w[0], x)) + math.exp(np.matmul(w[1], x)) + math.exp(np.matmul(w[2], x))))

print(prob)

