#!/usr/bin/env python
# coding: utf-8

# In[2]:


shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList)


# In[11]:


for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+\"+\"
        print(shoppingList[i])
    empty = []
    for i in empty:
           print(\"I am empty\")


# In[12]:


myList = [1,2,3,4,5,6,7]
print(myList)


# In[13]:


myList.insert(4,15)
print(myList)


# In[14]:


myList.append(55)
print(myList)


# In[15]:


newList = [11,12,13,14]
myList.extend(newList)
print(myList)


# In[16]:


def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

    print(searchinList(myList, 100))


# In[ ]:


total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
    
    print('Average:', average)


# In[ ]:


numlist = list() 
    while (True):
        inp = input('Enter a number: 
        if inp == 'done': break
        value = float(inp)
        numlist.append(value)
   
        average = sum(numlist) / len(numlist) 
    print('Average:', average)


# In[ ]:




