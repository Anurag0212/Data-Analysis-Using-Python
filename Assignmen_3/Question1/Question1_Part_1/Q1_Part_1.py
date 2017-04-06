
# coding: utf-8

# # Question 1 Part 1
# 
# - Use ‘vehicle_collisions’ data set. 
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City. 
# - Display a few rows of the output use df.head(). 
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[144]:

import pandas as pd
import numpy as np
from pandas import DataFrame as df


# In[145]:

#Importing csv file and storing data into vehicle_Collision variable
vehicle_collisions=pd.read_csv(r"Assignmen_3\Data\vehicle_collisions.csv") 


# In[146]:

vehicle_collisions['DATE']=pd.to_datetime(vehicle_collisions['DATE'])  #Converting DATE column to Datetime datatype
month_year_range=vehicle_collisions[vehicle_collisions['DATE'].isin(pd.date_range("01/01/16","12/31/16"))] #Storing data for the year 2016


# In[147]:

month_year_range['YEAR']=month_year_range['DATE'].dt.strftime('%Y/%b/%d').str.slice(0,4)
month_year_range['MONTH']=month_year_range['DATE'].dt.strftime('%Y/%b/%d').str.slice(5,8)  #Slicing month name from the month column


# In[156]:

manhattan_data=month_year_range[month_year_range.BOROUGH=='MANHATTAN']
manhattan_count=manhattan_data['BOROUGH'].value_counts().reset_index(drop=True)
manhattan_df=pd.DataFrame(manhattan_data.groupby(['MONTH'],sort=False).size().reset_index())
manhattan_df.columns=['MONTH','MANHATTAN_ACCIDENT_COUNT']
manhattan_df


# In[162]:

count_nyc=month_year_range['BOROUGH'].value_counts().reset_index(drop=True)
nyc_accident_count=pd.DataFrame(month_year_range.groupby(['MONTH'],sort=False).size().reset_index())
nyc_accident_count.columns=['MONTH','NYC_ACCIDENT_COUNT']
nyc_accident_count


# In[164]:

main_frame=pd.merge(manhattan_df,nyc_accident_count)
#frame
main_frame['PERCENTAGE']=(main_frame['MANHATTAN_ACCIDENT_COUNT']/main_frame['NYC_ACCIDENT_COUNT'])*100
main_frame


# In[166]:

main_frame.to_csv(r'Assignmen_3\Question1\Question1_Part_1\accident_count.csv',index=False)

