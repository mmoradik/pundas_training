
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[13]:

Index=['a','b','c','d']
obj=Series([3,6,9,12],index=Index)

obj


# In[3]:

obj.values
obj.index


# In[17]:

obj['c']


# In[6]:

obj[obj>6]


# In[7]:

3 in obj


# In[10]:

obj_dic=obj.to_dict()
obj_dic


# In[11]:

obj_series=Series(obj_dic)
obj_series


# In[19]:

Index=['a','b','c','d','e']
obj2=Series(obj,index=Index)
obj2


# In[21]:

pd.isnull(obj2)


# In[22]:

pd.notnull(obj2)


# In[25]:

obj2.index.name='alphabet'
obj2


# In[ ]:



