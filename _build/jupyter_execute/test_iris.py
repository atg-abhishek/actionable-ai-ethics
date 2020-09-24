#!/usr/bin/env python
# coding: utf-8

# # Test notebook for Iris dataset

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])


# In[3]:


data.head()


# In[ ]:




