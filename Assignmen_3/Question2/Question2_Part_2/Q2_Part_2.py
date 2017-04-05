
# coding: utf-8

# ## Question2 PART TWO
# 
# - Use 'employee_compensation' data set.
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# - Display the top 5 Job Families according to this percentage value using df.head().
# - Write the output (jobs and percentage value) to a csv.

# In[31]:

import pandas as pd
import numpy as np
from pandas import DataFrame as df


# In[32]:

employee_compensation=pd.read_csv(r'C:\Data Scienence\Assignmen_3\Data\employee_compensation.csv')  #reading csv file and storing values in a Variable
employee_compensation.head(3)


# In[33]:

employee_compensation=employee_compensation[employee_compensation['Year Type']=='Calendar']
employee_compensation.head()


# In[34]:

employee_salary_avg=employee_compensation.groupby(['Employee Identifier']).mean().reset_index()
employee_salary_avg.head()


# In[35]:

employee_salary_avg.to_csv(r'C:\Data Scienence\Assignmen_3\Question2\Question2_Part_2\employee_average_salary',index=False)


# In[36]:

overtime_salary=employee_compensation[employee_compensation['Overtime']>0.05*employee_compensation['Salaries']]
overtime_salary.head()


# In[37]:

job_family_group=pd.DataFrame(employee_compensation.groupby(['Job Family']).mean().reset_index())
job_family_group.head()


# In[41]:

job_family_group['Percentage']=(job_family_group['Total Benefits']/job_family_group['Total Compensation'])*100


# In[42]:

output_frame=job_family_group.drop(job_family_group.columns[[1,2,3,4,5,6,7,8,9,10,11]],axis=1)


# In[43]:

output_frame.head()


# In[44]:

output_frame.to_csv(r'C:\Data Scienence\Assignmen_3\Question2\Question2_Part_2\JobFamily_Percentage_benefit.csv',index=False)

