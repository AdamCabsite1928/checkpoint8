#!/usr/bin/env python
# coding: utf-8

# In[7]:


f = open("python.txt",'r',encoding = 'utf-8')
f.read()




# In[9]:


f = open("python.txt",'r',encoding = 'utf-8')
f.readline()


# In[11]:


f = open("python.txt",'r',encoding = 'utf-8')
f.readlines()[-1]


# In[18]:


f = open("python.txt",'r',encoding = 'utf-8')
d=f.read()
len(d.split(" "))


# In[ ]:




