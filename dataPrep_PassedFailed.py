__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.
    
    The intention of this code is to take an Open Data CSV file from DUO (duo.nl) containing raw data on the number of 
    passed and failed exams in middle schools in the Netherlands and create a new CSV file ready to be loaded into an
    Oracle Autonomous Data Warehouse for machine learning purposes. The only intend of using the specific data from DUO
    is to ensure we have a rich set of data to experiment with machine learning in combination with the Oracle 
    Autonomous Data Warehouse
    
    Source location for the raw data:
    https://duo.nl/open_onderwijsdata/databestanden/vo/leerlingen/leerlingen-vo-7.jsp
    
    IMPORTANT:
    do change the value of the variables:
        inputFileName  -- name (and path) for the input CSV file
        outputFileName -- name (and path) for the output CSV file
        measureYear    -- year (Peildatum) associated to the original file. 


'''

import csv
import uuid

inputFileName = "./rawData/passed_failed_2018.csv"
outputFileName = "./cleanData/passed_failed_2018.csv"
measureYear = "2018"



inputFile = csv.DictReader(open(inputFileName),delimiter=";")
with open(outputFileName, mode='w') as outputFile:

    # Construct the headers for the cleaned data
    cleanColumns = ['RECORD_UUID',
                    'MEASURE_YEAR',
                    'BRIN_NUMBER',
                    'LOCATION_NUMBER',
                    'LOCATION_NAME',
                    'LOCATION_CITY',
                    'LOCATION_PROVINCE',
                    'EDUCTION_TYPE',
                    'VMBO_EDUCATION_PATH',
                    'VMBO_SECTOR',
                    'DEPARTMENT',
                    'CANDIDATES_TOTAL',
                    'PASSED'
                    ]

    writer = csv.DictWriter(outputFile, fieldnames=cleanColumns,delimiter=';',)
    writer.writeheader()

    for row in inputFile:

        rawBrinNumber = row["BRIN NUMMER"]
        rawLocationNumber = row["VESTIGINGSNUMMER"]
        rawLocationName = row["INSTELLINGSNAAM VESTIGING"]
        rawLocationCity= row["GEMEENTENAAM VESTIGING"]
        rawLocationProvince= row["PROVINCIE VESTIGING"]
        rawEducationType= row["ONDERWIJSTYPE VO"]
        rawVmboEducationPath= row["LEERWEG VMBO"]
        rawVmboSector= row["VMBO SECTOR"]
        rawDepartment= row["AFDELING"]
        rawCandidatesTotal= row["EXAMENKANDIDATEN"]
        rawCandidatesPassed= row["GESLAAGDEN"]
        rawCandidatesFailed= row["GEZAKTEN"]
        rawAverageSchoolExame= row["GEMIDDELD CIJFER SCHOOLEXAMEN"]
        rawAverageCentralExame= row["GEMIDDELD CIJFER CENTRAAL EXAMEN"]
        rawAverageResults= row["GEMIDDELD CIJFER CIJFERLIJST"]

    # generate a new line for each individual failed candidate.
        loopFailed = 0
        while loopFailed < int(rawCandidatesFailed):
            writer.writerow({
                'RECORD_UUID' : uuid.uuid1(),
                'MEASURE_YEAR' : measureYear,
                'BRIN_NUMBER':rawBrinNumber,
                'LOCATION_NUMBER':rawLocationNumber,
                'LOCATION_NAME':rawLocationName,
                'LOCATION_CITY':rawLocationCity,
                'LOCATION_PROVINCE':rawLocationProvince,
                'EDUCTION_TYPE':rawEducationType,
                'VMBO_EDUCATION_PATH':rawVmboEducationPath,
                'VMBO_SECTOR':rawVmboSector,
                'DEPARTMENT':rawDepartment,
                'CANDIDATES_TOTAL':rawCandidatesTotal,
                'PASSED':'N'
            })
            loopFailed +=1

    # generate a new line for each passed candidate.
        loopPassed = 0
        while loopPassed < int(rawCandidatesPassed):
            writer.writerow({
                'RECORD_UUID': uuid.uuid1(),
                'MEASURE_YEAR': measureYear,
                'BRIN_NUMBER':rawBrinNumber,
                'LOCATION_NUMBER':rawLocationNumber,
                'LOCATION_NAME':rawLocationName,
                'LOCATION_CITY':rawLocationCity,
                'LOCATION_PROVINCE':rawLocationProvince,
                'EDUCTION_TYPE':rawEducationType,
                'VMBO_EDUCATION_PATH':rawVmboEducationPath,
                'VMBO_SECTOR':rawVmboSector,
                'DEPARTMENT':rawDepartment,
                'CANDIDATES_TOTAL':rawCandidatesTotal,
                'PASSED':'Y'
            })
            loopPassed +=1

    print ("done")