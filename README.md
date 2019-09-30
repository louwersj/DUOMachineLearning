# DUO Machine Learning
Machine Learning examples based upon data from DUO.nl

## Intention and use case
The main intention of this repository is to provide a number of things:
- Guidance and code on data preparation to be able to load data in an Oracle Autonomous Data Warehouse.
- Both a set of cleaned as well as raw data obtained from the duo.nl website
- Machine learning examples that make use of the data provided by duo.nl and which leverage the machine learning 
capabilities of the Oracle Autonomous Data Warehouse. 

The main use case for releasing both the data and the source code is to enable people to have a rapid start with 
exploring the machine learning capabilities of the Oracle Autonomous Data Warehouse and to allow the owner of this 
repository to share concepts and ideas in a tangible format. This repository will be referred to in a number of 
presentations and workshops to enable people to gain direct experience with the examples.

## Content
The below sections tries to provide some guidance on the content of this repository. 

### Data content
The data content stores the raw data used and in some cases the cleaned data as well. Main reason for inclusion of the 
data rather than referring ot it is that we want to ensure that the data is always available even in the case the 
original data source, the duo.nl website, stops to provide the data.
* Directory cleanData  
    *   passed_failed_* cleaned data for passed and failed students per year / per school
* Directory RawData 
    *   passed_failed_* raw data for passed and failed students per year / per school. This is the actual raw download 
    from the duo.nl website. 


### Code content
The code content section provides both machine learning examples as well as a number of data pre-processing and other 
utilities that have been developed over time while building the examples in this repository.

#### Data pre-processing  
* dataPrep_*.py
    * dataPrep_PassedFailed.py is used to take a raw passed_failed csv file and create a cleaned data file from it.
* dataMerge_*.p
    * dataMerge_PassedFailed.py is used to merge all clean passed_failed csv files into a single csv file.