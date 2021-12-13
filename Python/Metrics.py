#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np


# ### 3X3 Confusion Matrix

# In[2]:


confusion_matrix = [[31, 1, 3],[5, 30, 0], [6, 0, 29]]

conf = np.asarray(confusion_matrix)
d = conf.diagonal()
pred = np.sum(d)
accuracy = pred/np.sum(confusion_matrix) 

print(accuracy)


# ### 2X2 Confusion Matrix

# In[3]:


confusion_matrix = [[18, 12], [9,15]]

recall = confusion_matrix[0][0]/(confusion_matrix[0][0]+confusion_matrix[0][1])
precision = confusion_matrix[0][0]/(confusion_matrix[0][0]+confusion_matrix[1][0])
accuracy = (confusion_matrix[0][0]+confusion_matrix[1][1])/np.sum(confusion_matrix)

print('Recall: {:.2f}%'.format(recall*100))
print('Precision: {:.2f}%'.format(precision*100))
print('Accuracy: {:.2f}%'.format(accuracy*100))

