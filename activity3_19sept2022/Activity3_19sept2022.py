#!/usr/bin/env python
# coding: utf-8

# Notebook Created By : Tawheed Musaib

# 1.Count the number of alphabets in the given string

# In[12]:


givenStr = 'Welcome to Python World'
print('Original String:', givenStr)
num = len([ele for ele in givenStr if ele.isalpha()])
print('Number of Alphabets in string:', num)


# 2.Extract the characters in the given range from the given string

# In[13]:


givenStr = 'Welcome to Python World'
print('Original String:', givenStr)
start, end = 11, 25
resultStr = ''.join([ele for ele in givenStr])[start:end]
print('Extracted String:', resultStr)


# 3.Check Whether the given string is alphanumeric

# In[16]:


givenStr = 'Welcome to Python World'
if givenStr.isalnum():
    print('is alphanumeric.')
else:
    print('is not alphanumeric')


# 4.Calculate the length of string

# In[17]:


str1 = str(input("Enter the string: "))
print("Length of the given string is", len(str1))


# 5.Convert Later part of string to uppercase

# In[18]:


str2 = "tawheedmusaib"
str3 = str2[:6]
str4 = str2[6:].upper()

print(str3 + str4)


# In[ ]:




