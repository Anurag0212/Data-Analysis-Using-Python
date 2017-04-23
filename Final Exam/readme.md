# INFO 7374 Data Analysis Using Python - Final Project

## Data Analysis on Death Records of United States

I have downloaded the dataset from Kaggle to perform my Analysis on **Death Records**

There is a main Death record file which is like a fact table. It stores only keys, their corresponding records are stored in the separate csv file.


*Data Formats*

1.Death Records(CSV) - https://www.kaggle.com/cdc/mortality

### Data Collection and Processing

* There is a separate Data folder which stores the Raw data.

Location Raw Data: <a href="Other Files">Data</a>

* There are total 15 csv files which need to be merged together to create a processed csv file which is being used for the analysis.

Location Processed Data: <a href="Other Files">Processed Data</a>



## Analysis Performed


## Analysis 1 : Racial Bases survival rate in United States for Males and females

* Restricted the dataframe for Natural death cases
* Grouped the result on Race, Rasident status and Gender to get the count
* Plotted a grouped bar chart to display the result

<img width="751" alt="racial based survival" src="https://cloud.githubusercontent.com/assets/25333972/25310311/b078b73c-27af-11e7-92a3-f65e15a0d52f.PNG">

### Conclusion from Analysis 1:

* From this analysis we can say that the survival rate of Female's in any Race is always higher than the survival rate of Males in United States.




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
- There were only 588 cases where acciental victims werer dead on arrival to any medical center,clinic or Hospital, which is only 1.27% of cases
- From this analysis i can infere that the emegency response services in United states are faster and efficient.

** Statistics:**

    Total Accident Cases - 46072
    Dead on Arrival cases - 588



