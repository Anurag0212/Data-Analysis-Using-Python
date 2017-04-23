# INFO 7374 Data Analysis Using Python - Final Project

## Data Analysis on Death Records of United States

I have downloaded the dataset from Kaggle to perform my Analysis on **Death Records**
There is a main Death record file which is like a fact table. It stores only keys, their corresponding records are stored in the separate csv file.
There are total 24 csv files which need to be merged together to create a processed csv file which is being used for the analysis.

*Data Formats*

1.Death Records(CSV) - https://www.kaggle.com/cdc/mortality

### Data Collection and Processing

**Running the file**

Command : **python 'Data Collection and Processing.py' "City Name" "category name"**

Yelp Data categories have been specified above

**__Fetching the Data__**

* The API requests are placed to the Yelp API based on user search term to get related businesses
* The population data for these cities are fetched by placing a request to FullContact API.

**Storing the Data**

Yelp Data

 * Click <a href="Yelp Data">here</a> to view the data downloaded from Yelp
 * Files are segregated based on country and state.
 * Files are stored in json format.
    
Population Data
 * Click <a href="Population Data">here</a> to view the data downloaded from FullContact API
 * Files are segregated based by country.
 * Files are stored in json format.

**Post Process of data**


Yelp Data - Post Processing

* Storing the restaurant or hotel category and timings in separate CSV files.

Location: <a href="Other Files">Restaurant Category and Timings</a>

Population Data - Post Processing
* Joining population data and country abbreviations to form a consolidated data.

Location: <a href="Other Files">Consolidated Population Data</a>

**Creating the input file for performing analysis**

* The yelp data is merged with the population data (joining operations) based on location to get the final data to be analyzed

## Analysis Performed

**Running the file**

Command : **python Analysis.py**
