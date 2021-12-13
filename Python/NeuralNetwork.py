#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np


# ### ANN

# In[2]:


x = [1, 6.8, 225, 0.44, 0.68]

w1 = [[21.78, -1.65, 0, -13.26, -8.46], [-9.6, -0.44, 0.01, 14.54, 9.5]]
w2 = [2.84, 3.25, 3.46] 

ann = w2[0] + w2[1]*max(np.matmul(w1[0], x),0) + w2[2]*max(np.matmul(w1[1], x),0)

print(ann)

