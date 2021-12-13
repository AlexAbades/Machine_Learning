#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 

from scipy.cluster.hierarchy import linkage, fcluster, dendrogram


# ### Single (Minimum) Linkage

# In[6]:


X=[[0.0 ,2.91, 0.63, 1.88, 1.02, 1.82, 1.92, 1.58, 1.08, 1.43], 
   [2.91, 0.0, 3.23, 3.9, 2.88, 3.27, 3.48, 4.02, 3.08, 3.47],
   [0.63, 3.23, 0.0, 2.03, 1.06, 2.15, 2.11, 1.15, 1.09, 1.65],
   [1.88, 3.9, 2.03, 0.0, 2.52, 1.04, 2.25, 2.42, 2.18, 2.17],
   [1.02, 2.88, 1.06, 2.52, 0.0, 2.44, 2.38, 1.53, 1.71, 1.94],
   [1.82, 3.27, 2.15, 1.04, 2.44, 0.0, 1.93, 2.72, 1.98, 1.8],
   [1.92, 3.48, 2.11, 2.25, 2.38, 1.93, 0.0, 2.53, 2.09, 1.66],
   [1.58, 4.02, 1.15, 2.42, 1.53, 2.72, 2.53, 0.0, 1.68, 2.06],
   [1.08, 3.08, 1.09, 2.18, 1.71, 1.98, 2.09, 1.68, 0.0, 1.48],
   [1.43, 3.47, 1.65, 2.17, 1.94, 1.8, 1.66, 2.06, 1.48, 0.0]]

Method = 'single'
Metric = 'euclidean'

Z = linkage(X, method=Method, metric=Metric)

# Display dendrogram
#max_display_levels=6
plt.figure(2,figsize=(10,4))
#dendrogram(Z, truncate_mode='level', p=max_display_levels)
dendrogram(Z)

plt.show()


# In[3]:


X = [[0.00, 4.84, 0.50, 4.11, 1.07, 4.10, 4.71, 4.70, 4.93],
     [4.84, 0.00, 4.40, 5.96, 4.12, 2.01, 5.36, 3.59, 3.02],
     [0.50, 4.40, 0.00, 4.07, 0.72, 3.75, 4.66, 4.48, 4.64],
     [4.11, 5.96, 4.07, 0.00, 4.48, 4.69, 2.44, 3.68, 4.15],
     [1.07, 4.12, 0.72, 4.48, 0.00, 3.54, 4.96, 4.62, 4.71],
     [4.10, 2.01, 3.75, 4.69, 3.54, 0.00, 3.72, 2.23, 1.95],
     [4.71, 5.36, 4.66, 2.44, 4.96, 3.72, 0.00, 2.03, 2.73],
     [4.70, 3.59, 4.48, 3.68, 4.62, 2.23, 2.03, 0.00, 0.73],
     [4.93, 3.02, 4.64, 4.15, 4.71, 1.95, 2.73, 0.73, 0.00]]

Method = 'single'
Metric = 'euclidean'

Z = linkage(X, method=Method, metric=Metric)

# Display dendrogram
#max_display_levels=6
plt.figure(2,figsize=(10,4))
#dendrogram(Z, truncate_mode='level', p=max_display_levels)
dendrogram(Z, truncate_mode='level')

plt.show()


# ### Complete (Maximum) Linkage

# In[4]:


X = [[0, 0.534, 1.257, 1.671, 1.090, 1.315, 1.484, 1.253, 1.418],
     [0.534, 0, 0.727, 2.119, 1.526, 1.689, 1.214, 0.997, 1.056],
     [1.257, 0.727, 0, 2.809, 2.220, 2.342, 1.088, 0.965, 0.807],
     [1.671, 2.119, 2.809, 0, 0.601, 0.540, 3.135, 2.908, 3.087],
     [1.090, 1.526, 2.220, 0.601, 0, 0.331, 2.563, 2.338, 2.500],
     [1.315, 1.689, 2.342, 0.540, 0.331, 0, 2.797, 2.567, 2.708],
     [1.484, 1.214, 1.088, 3.135, 2.563, 2.797, 0, 0.275, 0.298],
     [1.253, 0.997, 0.965, 2.908, 2.338, 2.567, 0.275, 0, 0.343],
     [1.418, 1.056, 0.807, 3.087, 2.500, 2.708, 0.298, 0.343, 0]]

Method = 'complete'
Metric = 'euclidean'

Z = linkage(X, method=Method, metric=Metric)

# Display dendrogram
#max_display_levels=6
plt.figure(2,figsize=(10,4))
#dendrogram(Z, truncate_mode='level', p=max_display_levels)
dendrogram(Z, truncate_mode='level')

plt.show()


# ### Average Linkage

# In[5]:


X = [[5.7, 0], [6, 0], [6.2, 0], [6.3, 0], [6.4, 0], [6.6, 0], [6.7, 0], [6.9, 0], [7, 0], [7.4, 0]]

Method = 'average'
Metric = 'euclidean'

Z = linkage(X, method=Method, metric=Metric)

# Display dendrogram
#max_display_levels=6
plt.figure(2,figsize=(10,4))
#dendrogram(Z, truncate_mode='level', p=max_display_levels)
dendrogram(Z, truncate_mode='level')

plt.show()

