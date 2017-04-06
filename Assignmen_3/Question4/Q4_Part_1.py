
# coding: utf-8

# ## Q4_PART ONE 
# - Use ‘movies_awards’ data set.
# 
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below. 
# 
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.) 
# 
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# 
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# 
# - Create two separate columns for each award category (won and nominated). 
# 
# - Write your output to a csv file. (Sample output is given in next page)

# In[1]:

import pandas as pd
from pandas import DataFrame as df


# In[2]:

movies_awards=pd.read_csv(r'Assignmen_3\Data\movies_awards.csv')
movies_awards.head()


# In[3]:

movie_award=pd.DataFrame(movies_awards.groupby('Awards').size())
movie_award.columns=['count']
new_movie_frame=movie_award.reset_index()


# In[4]:

new_movie_frame.head()


# In[6]:

new_df = pd.DataFrame({'AWARDS':['FOO'],'AWARDS WON' : [0],'AWARDS NOMINATED' : [0],
                       'GOLDEN GLOBE WON' : [0],'GOLDEN GLOBE NOMINATED' : [0],
                       'OSCAR WON' : [0],'OSCAR NOMINATED' : [0],
                      'PRIMETIME EMMY WON' : [0],'PRIMETIME EMMY NOMINATED' : [0],
                      'BAFTA FILM WON' : [0],'BAFTA FILM NOMINATED' : [0]})
new_df.loc[0]
new_df


# In[7]:

for i in new_movie_frame.index:
    new_df.loc[i] = [new_movie_frame.ix[i]['Awards'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    str = new_movie_frame.ix[i]['Awards'].upper()
    index = str.find("WON")
    if index != -1:
        str = str[(index + 4):]
        splits = str.split()
        clm_name = splits[1].replace("OSCARS", "OSCAR")
        if(splits[1] == "BAFTA" or splits[1] == "GOLDEN" or splits[1] == "PRIMETIME"):
            clm_name += (" " + splits[2]).replace("GLOBES", "GLOBE").replace("EMMYS", "EMMY").replace("FILMS", "FILM")
        if(clm_name[-1] == '.'):
            clm_name = clm_name[:-1]
        
        new_df.set_value(i, clm_name + ' WON', splits[0])
        new_df.set_value(i, 'AWARDS WON', int(new_df.ix[i]['AWARDS WON']) + int(splits[0]))
    
    str = new_movie_frame.ix[i]['Awards'].upper()
    index = str.find("NOMINATED FOR")
    if index != -1:
        str = str[(index + 14):]
        splits = str.split()
        clm_name = splits[1].replace("OSCARS", "OSCAR")
        if(splits[1] == "BAFTA" or splits[1] == "GOLDEN" or splits[1] == "PRIMETIME"):
            clm_name += (" " + splits[2]).replace("GLOBES", "GLOBE").replace("EMMYS", "EMMY").replace("FILMS", "FILM")
        if(clm_name[-1] == '.'):
            clm_name = clm_name[:-1]
        
        new_df.set_value(i, clm_name + ' NOMINATED', splits[0])
        new_df.set_value(i, 'AWARDS NOMINATED', int(new_df.ix[i]['AWARDS NOMINATED']) + int(splits[0]))
    
    str = new_movie_frame.ix[i]['Awards'].upper()
    index = str.find("NOMINATION")
    if index != -1:
        str = str[:(index - 1)]
        splits = str.split()
        
        new_df.set_value(i, 'AWARDS NOMINATED', int(new_df.ix[i]['AWARDS NOMINATED']) + int(splits[len(splits) - 1]))
    
    str = new_movie_frame.ix[i]['Awards'].upper()
    index = str.find("WIN")
    if index != -1:
        str = str[:(index - 1)]
        splits = str.split()
        
        new_df.set_value(i, 'AWARDS WON', int(new_df.ix[i]['AWARDS WON']) + int(splits[len(splits) - 1]))    


# In[8]:

new_df.head()


# In[9]:

new_df.to_csv(r'Assignmen_3\Question4\movies_awards_output.csv',index=False)

