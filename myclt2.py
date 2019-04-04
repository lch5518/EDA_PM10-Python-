#!/usr/bin/env python
# coding: utf-8

# In[6]:


import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


def gamclt(n,a,b):
    x = []
    for i in range(1,101):
        x.append(np.mean(scipy.stats.gamma.rvs(a = a,scale = b,size = n)))
    x0 = np.asarray(x)
   
    
    st,cr,p = scipy.stats.anderson(x0, dist = 'norm')
    y = ''
    if st < cr[2]:
        y = 'normal dist'
    else:
        y = 'not normal dist'
    plt.hist(x0, bins = 10, rwidth = 0.85)  #bins : 막대기 개수
    plt.title('histogram, n = ' + str(n) +  "\n "+ str(y))


# In[10]:


get_ipython().system(' jupyter nbconvert --to python myclt2.ipynb')

