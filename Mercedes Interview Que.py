#!/usr/bin/env python
# coding: utf-8

# # Mercedes Interview Que

# ### Q1. Create a Dict , add elaments , modify an elem and print dict in alphabetical order of keys 

# In[2]:


# create dict
my_dict = {'name' :'Pratham' ,'age' : 26}
print(my_dict)


# In[3]:


# add elem
my_dict['occupation']  = 'Engineer'
my_dict['Package'] = '10 LPA'


# In[4]:


my_dict


# In[5]:


# modify dict
my_dict['Package'] = '12 LPA'
my_dict


# In[6]:


# print key in Alphabetical order
for key in sorted(my_dict):
    print(f"{key} : {my_dict[key]}")


# ### Q2 Find unique values in a list of assotrted numbers and print count of how many times each value is repeated 

# In[7]:


# Create list
my_list = [1,45,23,12,78,56,4,1,90,56,45,23,567,43,89,45,45,78,90,43,90,43,90]


# In[8]:


# create pandas Series
import pandas as pd
output = pd.Series(sorted(my_list))


# In[9]:


# freq of each value
count_of_each_value = output.value_counts()
count_of_each_value


# ### Q3 Find and print duplicate values in assorted numbers along with no of times each va;ue is repeated

# In[10]:


# Create list
my_list = [1,45,23,12,78,56,4,1,90,56,45,23,567,43,89,45,45,78,90,43,90,43,90]


# In[11]:


my_list = pd.Series(sorted(my_list))
my_list


# In[12]:


my_list.value_counts()


# In[13]:


# Find Duplicates
seen = set()
duplicates = set()

for num in my_list:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
#print(seen)
print(duplicates)


# In[14]:


# Count freq of each nos
import collections
from collections import Counter
counter = Counter(my_list)

# print counts of duplicates
for num in duplicates:
    print(f"{num} : {counter[num]}")


# ### Q4 Write a function to add 2 nos , take input from user and handle possible input errors such as non numeric input and empty i/p

# In[22]:


# function
def sum_of_2_num(num1 , num2):
    try:
        num1 = float(input('enter your 1st no '))
        num2 = float(input('enter your 2nd no '))
        return f"sum of given nos is {num1 + num2}"
    
    except ValueError:
        return "Invalid Input. Please enter numeric values"
    
    except Exception as e:
        return str(e)
    
sum_of_2_num(num1 ,num2)   


# In[ ]:




