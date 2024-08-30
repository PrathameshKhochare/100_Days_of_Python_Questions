#!/usr/bin/env python
# coding: utf-8

# # Infosys Interview Que

# In[1]:


# Data
import pandas as pd

# Sample data
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'Marketing', 'IT', 'HR', 'Marketing'],
    'Salary': [60000, 70000, 80000, 65000, 75000, 72000, 68000, 81000, 63000, 67000],
    'JoiningDate': ['2020-01-15', '2019-06-20', '2018-07-23', '2020-02-10', '2021-03-15',
                    '2019-11-30', '2020-08-12', '2021-01-07', '2022-02-28', '2021-10-19'],
    'PerformanceScore': [3, 4, 2, 5, 3, 4, 2, 5, 4, 3]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)


# ### 1. How can you calculate the average salary for each department?

# In[4]:


# avg_salary
avg_salary = df.groupby('Department')['Salary'].mean().reset_index().round(2)
avg_salary


# ### 2. Write a function to find the employee with the highest performance score in each department.

# In[10]:


# # Highest performance scorer
highest_performance_scorer = df.loc[df.groupby('Department')['PerformanceScore'].rank(ascending = False) == 1]
highest_performance_scorer


# In[11]:


#OR


# In[13]:


# Highest performance scorer
highest_performance_scorer = df.loc[df.groupby('Department')['PerformanceScore'].idxmax()]
highest_performance_scorer


# ### 3. How would you add a new column that represents the number of years each employee has been with the company based on the JoiningDate?

# In[14]:


df.head()


# In[23]:


from datetime import datetime

#calculate total years in company
df['years_since_joining'] = (pd.to_datetime('today') -  pd.to_datetime(df['JoiningDate'])).dt.days // 365

# or
df['years_since_joining_date'] = (datetime.now() -  pd.to_datetime(df['JoiningDate'])).dt.days // 365


# In[96]:


# Calculate the number of months with the company
curr_date = datetime.now()
df['months_with_company'] = (curr_date.year - pd.to_datetime(df['JoiningDate']).dt.year) * 12 + (curr_date.month - pd.to_datetime(df['JoiningDate']).dt.month)
df


# In[36]:


datetime.now()


# In[20]:


pd.to_datetime('today')


# ### 4. Create a pivot table to display the total salary and average performance score for each department.

# In[46]:


df.pivot_table( values = ['Salary' ,'PerformanceScore'] , index = 'Department' , aggfunc = {'Salary': 'sum' , 'PerformanceScore': 'mean'}).rename(columns = {'Salary': 'total_sal' , 'PerformanceScore': 'avg_performance_score'})


# ### 5. How would you create a new DataFrame containing only the employees from the IT department who have a performance score greater than 3?

# In[47]:


df


# In[54]:


new_df = df[ (df['Department'] == 'IT') & (df['PerformanceScore'] > 3) ]
new_df


# ### 6. Describe how to perform an inner merge of this DataFrame with another DataFrame containing employee bonus information based on EmployeeID.

# In[55]:


bonus_data = {'EmployeeID': [1, 2, 3, 4, 5], 'Bonus': [5000, 7000, 6000, 6500, 8000]}
bonus_df = pd.DataFrame(bonus_data)
bonus_df


# In[57]:


merged_df = pd.merge(df , bonus_df ,how = 'inner' , on = 'EmployeeID' )
merged_df


# ### 7. How can you calculate the cumulative sum of the PerformanceScore column grouped by Department?

# In[62]:


df.head()


# In[78]:


# Calculate cumulative sum of PerformanceScore within each Department
df['performance_score_cummm_sum'] = df.groupby('Department')['PerformanceScore'].cumsum()

# Sort the DataFrame by emp_id
sorted_df = df.sort_values(by = 'Department')
sorted_df


# ### 8. Write a function to rank employees within each department based on their Salary.

# In[88]:


df['ranking'] = df.groupby('Department')['Salary'].rank(ascending = False)
df.sort_values(by = ['Department','ranking'] , ascending = [True ,True])


# ### 9. How can you filter the DataFrame to show only employees who have been with the company for more than 2 years?

# In[93]:


# more than 2 years emp
filtered_df = df.loc[ (pd.to_datetime('today') - pd.to_datetime(df['JoiningDate'])).dt.days // 365 > 2]
filtered_df


# # end

# In[ ]:




