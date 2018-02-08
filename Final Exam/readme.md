# INFO 7374 Data Analysis Using Python - Final Project

## Data Analysis on Death Records of United States

I have downloaded the dataset from Kaggle to perform my Analysis on **Death Records**

There is a main Death record file which is like a fact table. It stores only keys, their corresponding records are stored in the separate csv file.


*Data Formats*

1.Death Records(CSV) - https://www.kaggle.com/cdc/mortality

### Data Collection and Processing

* There is a separate Data folder which stores the Raw data.

Location Raw Data: <a href="https://github.com/Anurag0212/singh_Anurag_Spring17/tree/master/Final%20Exam/Data">Data</a>

* There are total 15 csv files which need to be merged together to create a processed csv file which is being used for the analysis.

Location Processed Data: <a href="https://github.com/Anurag0212/singh_Anurag_Spring17/tree/master/Final%20Exam/Processed%20Data">Processed Data</a>



## Analysis Performed


## Analysis 1 : Racial Bases survival rate in United States for Males and females

* Restricted the dataframe for Natural death cases
* Grouped the result on Race, Rasident status and Gender to get the count
* Plotted a grouped bar chart to display the result

<img width="751" alt="racial based survival" src="https://cloud.githubusercontent.com/assets/25333972/25310311/b078b73c-27af-11e7-92a3-f65e15a0d52f.PNG">

### Conclusion from Analysis 1:

* From this analysis we can say that the **survival rate of Female's in any Race is always higher than the survival rate of Males in United States**.




## Analysis 2 : Performed analysis to check the response time of Emergency Services in United States

* Imported data from the processed data file
* Grouped the data on Manner of Death column
* Calculated total number of death cases registered for the year 2014
* Extracted only those records where manner of death was **Accident**.
* Displayed distribution of Accidental death based on place of death and decedents status
* Plotted a bar chart and highlighted the bar were place of death was - Dead on Arrival.

<img width="764" alt="emergency response time" src="https://cloud.githubusercontent.com/assets/25333972/25309862/edc1e758-27a5-11e7-9517-76032016bc92.PNG">

### Conclusion from Analysis 2:

- Total **46072** accidental cases have been recorded in 2014
- There were only **588** cases where acciental victims werer dead on arrival to any medical center,clinic or Hospital, which is only **1.27%** of cases
- From this analysis i can infere that the emegency response services in United states are faster and efficient.

** Statistics from analysis 2:**

    Total Accident Cases - 46072
    Dead on Arrival cases - 588



## Analysis 3 : Finding the Death trends for each months

* Imported data from the processed data file
* Merged processed csv file with another file to get the **Month Name** instead of month number.
* Assigned proper column name to my new dataframe
* Extracted data for records present in manner of death column to find the trend
* Plotted a line graph to find the trend between Suicidal, Accidental and Homicidal deaths.

<img width="760" alt="trend analysis" src="https://cloud.githubusercontent.com/assets/25333972/25310423/c7ced4e6-27b1-11e7-9bfd-7263300343cd.PNG">


### Conclusion from Analysis 3:

- Accidental deaths are higher than the suicidal and homicidal deaths in United States
- Accidental deaths were higher in the month of **January** and **July** as per our analysis
- Suicidal deaths were higher in the month of **September**




## Analysis 4 : Suicidal Cases based on persons educational level

* Imported data from the processed data file
* Restricted my dataframe to show only those record where Manner of death was Suicide.
* Grouped my dataframe based on the Educational level column.
* Stored the data in a csv file as a result of this analysis
* Created a pie chart to display the percetage of suicidal deaths based on the educational level.

<img width="674" alt="suicidal cases based on education level" src="https://cloud.githubusercontent.com/assets/25333972/25310456/8d725128-27b2-11e7-9601-d7fe775d291e.PNG">


### Conclusion from Analysis 4:

- More than **15 thousand suicidal cases** have been recorded in the year 2014
- Out of all the cases **38.2% of high school graduate students** have commited suicide
- Less than **3%** of Doctorate or professional degree holder have commited suicide in 2014

**Statistics:**

    Category Type    -      Category                   -     Percentage of Suicidal Deaths

    Highest          -      High School Graduate       -     38.2%

    Lowest           -      Doctorate or Professional  -     2.04%
    
    
 ## Analysis 5 : Homicidal cases based on Marital Status and gender

* Imported data from the processed data file
* Restricted my dataframe to show only those record where Manner of death was Homicide.
* Grouped my dataframe based on the Marital status and gender coulmns.
* Stored the data in a csv file as a result of this analysis
* Created a grouped bar chart to display the homicidal deaths bassed on their **marital status** and **gender**.


<img width="404" alt="homicidal deaths" src="https://cloud.githubusercontent.com/assets/25333972/25310487/5c20e9ee-27b3-11e7-9997-57ab487c17c3.PNG">



### Conclusion from Analysis 5:

* From the dataset of Death records, I can infer that Males are targeted in the homicidal cases in United States.
* Total **'6639'** cases of homicidal deaths was recorded, out of that **80.46%** were males.
* Out of those 80% males, Marital status of **71% of males** were **'Never Married, Single'**.

**Statistics:**
* Total Homicide Cases = 6639
* Male =   5342      - 80.46%
* Female=  1297      - 19.54%

**Never Married, Single Male = 3776**
