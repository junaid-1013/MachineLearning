#!/usr/bin/env python
# coding: utf-8

# ## Assignment 01
# ### Junaid Ali Bhatti
# ### FA24-RCS-005

# ### Task 1

# In[7]:


#Task 1.1
nums = [3, 5, 7, 8, 12]
cubes=[]
for a in nums:
    cubes.append(a**3)
cubes


# In[11]:


#Task 1.2
dict = {}
dict["parrot"]=2
dict["goat"]=4
dict['spider']=8
dict["crab"]=10
dict


# In[24]:


#Task 1.3
print("---------------")
print("Animal\t","Legs")
print("---------------")
sum=0

for x,y in dict.items():
    print(x,"\t",y)
    sum=sum+y
    
print("---------------")
print("Total\t",sum)
print("---------------")


# In[38]:


#Task 1.4
A = (3, 9, 4, [5, 6])
A[3][0]=8  #chaning value from 5 to 8.
A


# In[39]:


#Task 1.5
del A


# In[50]:


#Task 1.6
B = ('a', 'p', 'p', 'l','e')
sum=0
for a in B:
    if(a=='p'):
        sum=sum+1
print("No of Acurance of in B: ",sum)


# In[53]:


#Task 1.7
B.index('l')


# ### Task 2

# In[54]:


import numpy as np


# In[58]:


#Task 2.1
A=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
A


# In[60]:


#Task 2.2
b=A[:2,:2]
b


# In[72]:


#Task 2.3
c=np.empty(A.shape)


# In[73]:


#Task 2.4
z = np.array([1, 0, 1])
for i in range(A.shape[1]):
    c[:, i] = A[:, i] + z
c


# In[74]:


X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
v = np.array([9,10])


# In[77]:


#Task 2.5
np.add(X,Y)


# In[78]:


#Task 2.6
np.dot(X,Y)


# In[79]:


#Task 2.7
np.sqrt(Y)


# In[80]:


#Task 2.8
np.dot(X,v)


# In[86]:


#Task 2.9
np.sum(X,axis=0)


# ### Task 3

# In[89]:


#Task 3.1
def Compute(distance,time):
    return distance/time
#e.g
print("Velocity: ",Compute(10,2),"m/s")


# In[91]:


#Task 3.2
even_num=[2,4,6,8,10,12]
def mul(even_num):
    prod=1
    for i in even_num:
        prod=prod*i
    return prod
print("Product of elemects of list: ",even_num," is: ",mul(even_num))


# ### Task 4

# In[96]:


import pandas as pd
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}
df = pd.DataFrame(data)
df


# In[97]:


#Task 4.1
df.head(2)


# In[98]:


#Task 4.2
df['C2']


# In[99]:


#Task 4.3
df.rename(columns={'C3': 'B3'}, inplace=True)
df


# In[101]:


#Task 4.4 , 4.5
df['Sum'] = df.sum(axis=1)
df


# In[102]:


#Task 4.6
df1=pd.read_csv('hello_sample.csv')


# In[103]:


#Task 4.7
df1


# In[104]:


#Task 4.8
df1.tail(2)


# In[105]:


#Task 4.9
df1.info()


# In[107]:


#Task 4.10
df1.shape


# In[108]:


#Task 4.11
df1.sort_values(by='Weight')


# In[110]:


#Task 4.12
df1.isnull()


# In[111]:


df1.dropna()


# ##### No they did'nt make any changes as there are no null values

# In[ ]:




