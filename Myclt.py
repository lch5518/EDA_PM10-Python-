#!/usr/bin/env python
# coding: utf-8

# ## 동전 100회

# * array와 list의 가장 큰 차이점은 행열 이름의 유무

# In[118]:


import numpy as np
#import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import scipy.stats


# In[120]:


x = [0,1]


# <br>
# ~B(5,0.5)

# In[121]:


rd.choices(x,k = 5)


# <br>
# ~B(20,0.5)<br>
# x=20일때 평균 : 20/2, 분산 : 100/4

# In[122]:


rd.choices(x,k=20)


# In[115]:


def clt(n):
    x = [0,1]
    g = []
    
    for i in range(1,101):
        g.append(sum(rd.choices(x,k=n)))
        
        #print(g)
        #print(i," : ",sum(rd.choices(x,k=5)))
    g0 = np.asarray(g)
    #type(g0)
    
    plt.hist(g0, bins = 10, rwidth = 0.85)  #bins : 막대기 개수
    plt.title('histogram, n = ' + str(n))
    
    st,cr,p = scipy.stats.anderson(g0, dist = 'norm')

    if st < cr[2]:
        print('normal dist')
    else:
        print('not normal dist')
        
    #print(scipy.stats.anderson(g0, dist = 'norm'))


# In[116]:


clt(20)


# * statistic : 검정통계량
# * critical_values : 유의확률
# * significance_level : 유의수준(15%, 10%, 5%, 2.5%, 1%)
# <br>
# 
# ##### critical_values이 5%보다 크면 귀무가설 기각

# In[106]:


scipy.stats.anderson(g0, dist = 'norm')


# In[108]:


st,cr,p = scipy.stats.anderson(g0, dist = 'norm')

print(st)
print(cr)
print(p)


# In[109]:


cr[2]


# * 모듈 만들기

# In[119]:


get_ipython().system(' jupyter nbconvert --to python Myclt.ipynb')

