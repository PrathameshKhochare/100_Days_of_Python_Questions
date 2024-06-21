#!/usr/bin/env python
# coding: utf-8

# # Day 1 

# #### Q. Find out largest of 3 nos

# In[13]:


num1 = float(input('enter 1st no '))
num2 = float(input('enter 2nd no '))             
num3 = float(input('enter 3rd no '))

if num1 > num2 :
    if num1 > num3:
        print('largest no is',num1)
elif num2 > num3:
    print('largest no is',num2)
else:
    print('largest no is',num3)


# In[ ]:




