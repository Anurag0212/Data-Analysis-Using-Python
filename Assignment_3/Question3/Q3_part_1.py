
# coding: utf-8

# # Question 3 Part One
# - Use ‘cricket_matches’ data set. 
# - Calculate the average score for each team which host the game and win the game. 
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition. 
# - Display a few rows of the output use df.head() 
# - Generate a csv output.

# In[182]:

import pandas as pd
import numpy as np
from pandas import DataFrame as df


# In[183]:

match_data=pd.read_csv(r'Assignmen_3\Data\cricket_matches.csv')  #reading csv file and storing values in a Variable
print(match_data.head(3))


# In[184]:

filtered_data=match_data[match_data.home==match_data.winner]  #Applying filter to get the team names who hosts and wins the game
print(filtered_data.head(3))


# In[185]:

host_winning_match=pd.DataFrame(filtered_data.groupby('home').size().reset_index())  #Couting how many time a team hosts and wins the game
host_winning_match.columns=['Home','Number']                                         #Giving column names to the new data frame
print(host_winning_match.head(5))


# In[186]:

winners_first_inning=filtered_data.groupby('home').apply(lambda x: x[x['winner']==x['innings1']]['innings1_runs'].sum())
winners_second_inning=filtered_data.groupby('home').apply(lambda x: x[x['winner']==x['innings2']]['innings2_runs'].sum())


# In[193]:

Score=winners_first_inning+winners_second_inning
Score=pd.DataFrame(Score.reset_index())
Score.columns=['Home','Score']
print(Score.head(5))


# In[201]:

average_score=pd.merge(host_winning_match,Score)
average_score['Average Score']=(average_score['Score']/average_score['Number'])
print(average_score.head(5))


# In[202]:

average_score=average_score.drop(average_score.columns[[1,2]],axis=1)


# In[203]:

print(average_score.head())


# In[204]:

average_score.to_csv(r'Assignmen_3\Question3\Team_average_score.csv',index = False)

