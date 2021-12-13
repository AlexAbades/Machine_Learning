#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math


# ### Plot

# In[2]:


mean = [0, 0]
cov = [[0.0035, 0.0003], [0.0003, 0.003]]

x, y = np.random.multivariate_normal(mean, cov, 20000).T
plt.plot(x, y, 'x')
plt.show()


# ### Gaussian Mixture Probability

# In[3]:


X = 6.9
K = 3

w = [0.37, 0.29, 0.34]
m = [6.12, 6.55, 6.93]
s = [0.09, 0.13, 0.12]

p=[]

for i in range(K):
    temp = w[i]*(1/np.sqrt(2*math.pi*s[i]))*math.exp(-1/(2*s[i])*np.power(X-m[i], 2))
    p.append(temp)
    
#Probability for a Cluster 
def prob(p, k):
    pr = p[k-1]/np.sum(p)
    return pr

#Select Cluster
probability = prob(p, 2)
print(probability)


# In[4]:


#Gaussian Mixture with squared sigma
X = 15.38
K = 3

w = [0.13, 0.55, 0.32]
m = [18.347, 14.997, 18.421]
s = [1.2193, 0.986, 1.1354]
s = np.power(s, 2)

p=[]

for i in range(K):
    temp = w[i]*(1/np.sqrt(2*math.pi*s[i]))*math.exp(-1/(2*s[i])*np.power(X-m[i], 2))
    p.append(temp)
    
#Probability for a Cluster 
def prob(p, k):
    pr = p[k-1]/np.sum(p)
    return pr

#Select Cluster
probability = prob(p, 2)
print(probability)


# In[5]:


#Gaussian Mixture with squared sigma
X = 3.19
K = 3

w = [0.19, 0.34, 0.48]
m = [3.177, 3.181, 3.184]
s = [0.0062, 0.0076, 0.0075]
s = np.power(s, 2)

p=[]

for i in range(K):
    temp = w[i]*(1/np.sqrt(2*math.pi*s[i]))*math.exp(-1/(2*s[i])*np.power(X-m[i], 2))
    p.append(temp)
    
#Probability for a Cluster 
def prob(p, k):
    pr = p[k-1]/np.sum(p)
    return pr

#Select Cluster
probability = prob(p, 2)
print(probability)

