#!/usr/bin/env python
# coding: utf-8

# In[1]:


array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]
print(array)


# In[2]:


print(array[0])


# In[3]:


print(array[2])


# In[4]:


print(array[0][2])


# In[5]:


print(array[2][3])


# In[8]:


array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]
array.insert(2, [1,2,3,4,5])
array.insert(2, [1,2,3,4,5])
array.insert(2, [1,2,3,4,5])
print(array)


# In[19]:


twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)


# In[17]:


newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[22]:


print(len(twoDArray))


# In[20]:


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)


# In[21]:


print(len(newTwoDArray))


# In[23]:


print(len(newTwoDArray[0]))


# In[26]:


def accessElements(array, rowIndex, colIndex):
       if rowIndex >= len(array) or colIndex >= len(array[0]):
            print('Incorrect Index')
       else:
            print(array[rowIndex][colIndex])


# In[27]:


accessElements(newTwoDArray, 1, 2)


# In[28]:


def traverseTDArray(array):
       for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# In[29]:


traverseTDArray(twoDArray)


# In[30]:


def searchTDArray(array, value):
        for i in range(len(array)):
               for j in range(len(array[0])):
                if array[i][j] == value:
                    return 'The value is located index '+str(i)+\" \"+str(j)
        return 'The element no found'


# In[31]:


print(twoDArray)


# In[32]:


print(searchTDArray(twoDArray, 12))


# In[33]:


newTDArray = np.delete(twoDArray, 2, axis=0)
print(newTDArray)


# In[34]:


print(twoDArray)


# In[ ]:




