#!/usr/bin/env python
# coding: utf-8

# In[33]:


x="boat"
y=list(x)
print(y)
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(y,0,2)
str=""
z=str.join(y)
print(z)


# In[34]:


a='create'
b=list(a)
print(b)
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
swap(b,1,4)
str=""
c=str.join(b)
print(c)


# In[39]:


a1='create'
b1=list(a1)
print(b1)
def swap(list,pos1,pos2,pos3):
    list[pos1],list[pos2],list[pos3]=list[pos3],list[pos1],list[pos2]
    return list
swap(b1,1,3,5)
str=""
c1=str.join(b1)
print(c1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




