#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np


# ### Weights

# In[2]:


w1 = [0.0538, 0.0558, 0.1861, -0.0596]
w2 = [0.0089, 0.0931, 0.1093, 0.0417]
w3 = [0.2811, 0.0445, 0.3379, -0.4626]
w4 = [0.0167, 0.0698, 0.1354, 0.0403]

w1 = np.sum(np.square(w1))
w2 = np.sum(np.square(w2))
w3 = np.sum(np.square(w3))
w4 = np.sum(np.square(w4))

print('\n', w1, '\n', w2 , '\n', w3, '\n', w4)


# **Comment:** The maximum weight is assigned to the minimum $\lambda$

# In[ ]:




