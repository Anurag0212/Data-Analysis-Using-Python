
# coding: utf-8

# # Question 2 Part 1
# 
# - Use 'employee_compensation' data set. 
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department. 
# - Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value. 
# - Display a few rows of the output use df.head()

# In[55]:

import pandas as pd
import numpy as np
from pandas import DataFrame as df


# In[57]:

employee_compensation=pd.read_csv(r'C:\Data Scienence\Assignmen_3\Data\employee_compensation.csv')  #reading csv file and storing values in a Variable
employee_compensation.head(3)


# In[58]:

organization_group=pd.DataFrame(employee_compensation.groupby(['Organization Group','Department'])['Total Compensation'].mean())
organization_group_index=organization_group.reset_index()
sorted_compensation=organization_group_index.groupby(['Organization Group']).apply(lambda x: x.sort_values(['Total Compensation'],ascending=False))


# In[59]:

del sorted_compensation['Organization Group']


# In[60]:

sorted_compensation.head(9)


# In[61]:

sorted_compensation.to_csv(r'C:\Data Scienence\Assignmen_3\Question2\Question2_Part_1\employee_compensation_output.csv')

