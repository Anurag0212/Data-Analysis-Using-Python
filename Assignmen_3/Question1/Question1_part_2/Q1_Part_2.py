
# coding: utf-8

# # Question 1 Part 2
# - Use ‘vehicle_collisions’ data set. 
# - For each borough, find out distribution of each collision scale. (One car involved? Two? Three? or more?) (From 2015 to present) 
# - Display a few rows of the output use df.head(). 
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'twovehicles', 'three-vehicles', 'more-vehicles')

# In[1]:

import pandas as pd
import numpy as np
from pandas import DataFrame as df


# In[2]:

#Importing csv file and storing data into vehicle_Collision variable
vehicle_collisions=pd.read_csv(r"Assignmen_3\Data\vehicle_collisions.csv") 
print(vehicle_collisions.head())


# In[3]:

vehicle_collisions['BOROUGH']=pd.DataFrame(vehicle_collisions['BOROUGH'].fillna(value='Unknown Borough'))  #Replacing Null by a String Value for BOROUGH column 


# In[4]:

vehicle_collisions=vehicle_collisions.fillna(value=0)   #Replacing Null by 0 in Dataframe 
print(vehicle_collisions.head())


# In[5]:

vehicle1=vehicle_collisions['VEHICLE 1 TYPE'].apply(lambda x: 1 if x else 0)   #Assign value 1 where ever vehicle 1 type is not null else 0
vehicle2=vehicle_collisions['VEHICLE 2 TYPE'].apply(lambda x: 1 if x else 0)   #Assign value 1 where ever vehicle 1 type is not null else 0
vehicle3=vehicle_collisions['VEHICLE 3 TYPE'].apply(lambda x: 1 if x else 0)   #Assign value 1 where ever vehicle 1 type is not null else 0
vehicle4=vehicle_collisions['VEHICLE 4 TYPE'].apply(lambda x: 1 if x else 0)   #Assign value 1 where ever vehicle 1 type is not null else 0
vehicle5=vehicle_collisions['VEHICLE 5 TYPE'].apply(lambda x: 1 if x else 0)   #Assign value 1 where ever vehicle 1 type is not null else 0


# In[6]:

vehicle_collisions['Total']=vehicle1+vehicle2+vehicle3+vehicle4+vehicle5  #Adding Columns and storing the values to a new column


# In[7]:

accident_count=pd.DataFrame(vehicle_collisions.groupby(['BOROUGH','Total']).size().reset_index())  #Grouping BOROUGH and Vehicle involved in accident and counting the values
accident_count.columns=['BOROUGH','TOTAL','COUNT']     #Assigning columns names to new Dataframe
print(accident_count.head())


# In[8]:

new_df = pd.DataFrame({'BOROUGH' : ["FOO"],'ONE_VEHICLE_INVOLVED' : [0],'TWO_VEHICLES_INVOLVED' : [0],
                       'THREE_VEHICLES_INVOLVED' : [0], 'MORE_VEHICLES_INVOLVED' : [0]})
new_df.loc[0]
new_df
counter = 0
for i in accident_count.index:
    if(len(list(np.where(new_df['BOROUGH'] == accident_count.ix[i]['BOROUGH'])[0])) != 0):
        index = list(np.where(new_df['BOROUGH'] == accident_count.ix[i]['BOROUGH'])[0])
        if(accident_count.ix[i]['TOTAL'] == 1):
            new_df.set_value(index, 'ONE_VEHICLE_INVOLVED', accident_count.ix[i]['COUNT'])
        elif(accident_count.ix[i]['TOTAL'] == 2):
            new_df.set_value(index, 'TWO_VEHICLES_INVOLVED', accident_count.ix[i]['COUNT'])
        elif(accident_count.ix[i]['TOTAL'] == 3):
            new_df.set_value(index, 'THREE_VEHICLES_INVOLVED', accident_count.ix[i]['COUNT'])
        elif(accident_count.ix[i]['TOTAL'] == 4):
            new_df.set_value(index, 'MORE_VEHICLES_INVOLVED', new_df.ix[index]['MORE_VEHICLES_INVOLVED'] + accident_count.ix[i]['COUNT'])
        elif(accident_count.ix[i]['TOTAL'] == 5):
            new_df.set_value(index, 'MORE_VEHICLES_INVOLVED', new_df.ix[index]['MORE_VEHICLES_INVOLVED'] + accident_count.ix[i]['COUNT'])
    else:
        new_df.loc[counter] = [accident_count.ix[i]['BOROUGH'], 0, 0, 0, 0]
        counter = counter + 1


# In[9]:

new_df=new_df[['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']]
print(new_df)


# In[11]:

new_df.to_csv(r'Assignmen_3\Question1\Question1_part_2\vehicle_output.csv',index=False)

