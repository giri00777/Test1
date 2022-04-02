#!/usr/bin/env python
# coding: utf-8

# In[15]:


from operator import and_
from functools import reduce
given_sets = [{1,2,3,4,8},{2,3,8,5,6},{8,4,5,3,7},{6,9,8,3},{9,12,3,7,6,8,4,6,21,1,6}]  
print("The original list is : " + str(given_sets))  
res = set(reduce(and_ ,given_sets))
print("Intersected Sets : " + str(res))


# In[23]:


positive=['good','awesome','best','nice']
negative=['worst','awful']
comments=['He is a good boy','Food is the worst here','He is an awesome player','She is the best','This pizza tastes awful','These burger are really nice']
Com1=comments[0]+" - "+positive[0]
Com2=comments[1]+ " - "+negative[0]
Com3=comments[2]+" - "+positive[1]
Com4=comments[3]+" - "+positive[2]
Com5=comments[4]+" - "+negative[1]
Com6=comments[5]+" - "+positive[3]
print(Com4)


# In[16]:


def value(n):
    d = { 'Square': lambda a : a**2, 
         'Cube': lambda a : a**3, 
         'Squareroot': lambda a : a**(1/2)}       
    sum = 0
    for key in d.keys():
        sum += d[key](n)
    return sum
    
print(value(4))


# In[26]:


fruits=(('Lemon',"sour"),('DragonFruit','sweet'),('Grapes','sour'),('Kiwi','sour'),('Apples','sweet'),('Orange','sour'),('Blueberries','sweet'),('Limes','sour'))
s="sour"
for i in fruits:
    for n in i:
        if(n==s):
            print(i)


# In[27]:


a=[9,5,7,8,5]
from  itertools import accumulate
result=accumulate(a,lambda x,y:(x+y)/2)
for res in result :
    print(res)


# In[28]:


Is=['True','FALse','tRue','False','faLse']
list(map(lambda a:a.upper(),Is))


# In[33]:


import datetime.
date = '2021-05-21'
print(date. year) 


# In[ ]:





# In[ ]:




