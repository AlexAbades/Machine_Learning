#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
x = np.array([-2.1, -1.7, -1.5, -0.4, 0, 0.6, 0.8, 1, 1.1, 7.4 ])


# In[28]:


# We suspect that O-10 is an outlier:
k = 3
total_lists = [[] for i in range(k+1)]
densities = [[] for i in range(k+1)]
for i in range(k+1):
    list1 = x - x[len(x)-1-i]
    list2 = np.sort([abs(x) for x in list1])
    total_lists[i] = list2


# In[29]:


for i in range(k+1):
    density = []
    for j in range(1,k+1):
        #print(total_lists[i][j])
        den = (1/k) * (total_lists[i][j])
        density.append(den)
    s = sum(density)
    densities[i].append(1/s)


# In[30]:


s1 = 0
for i in range (1, k+1):
    #print(densities[i][0])
    s1 = s1 + densities[i][0]

final_density = densities[0][0]/((1/3)*s1)
final_density


# In[ ]:




