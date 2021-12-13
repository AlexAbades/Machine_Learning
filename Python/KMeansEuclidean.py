#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np

from sklearn.cluster import k_means


# ### Functions

# In[2]:


def kmeans2_main(data, centroids):
    c1, c2 = centroids
    dif1, dif2 = data - c1, data - c2
    cat1, cat2 = [], []

    for i in range(0, len(data)):
        if abs(dif1[i]) <= abs(dif2[i]):
            cat1.append(data[i])
        elif abs(dif2[i]) <= abs(dif1[i]):
            cat2.append(data[i])
        else:
            print("ERROR")

    # Print clusterings
    print(cat1, cat2)

    # Return new centroids
    return np.array([np.mean(cat1), np.mean(cat2)])

def kmeans2(data, centroids):
    current = np.array(centroids)
    old = np.zeros(2)
    while np.any(current != old):
        old = current
        current = kmeans2_main(data, current)
    print("terminated!\ncentroids:", current)


# ### Converged

# In[3]:


X = [[1, 0], [3, 0], [4, 0], [6, 0], [7, 0], [8, 0], [13, 0], [15, 0], [16, 0], [17, 0]]
X = np.asarray(X)
K = 3

centroids, cls, inertia = k_means(X,K)

print(cls)


# In[4]:


X = [[5.7, 0], [6, 0], [6.2, 0], [6.3, 0], [6.4, 0], [6.6, 0], [6.7, 0], [6.9, 0], [7, 0], [7.4, 0]]
X = np.asarray(X)
K = 2

centroids, cls, inertia = k_means(X,K)

print(cls)


# ### Selected Centroids

# In[5]:


X = [19.4, 30.3, 34.2, 38.3, 40.1, 42, 50.9, 68.6]
X = np.asarray(X)

c = [19.4, 30.3]

kmeans2(X, c)

