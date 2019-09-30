__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    The intention of this code is to take all passed_failed CSV files that each describe a single year of DUO data and 
    merge it into one single .csv file. 
    
    Assumptions:
    - The csv delimiter is ;
    - All files are located under ./cleanData
    - All files are named passed_failed_****.csv 
    - All files are correctly cleaned data
    
    Special thanks:
    - Ekapope Viriyakovithya -- https://ekapope.github.io/
'''

import os
import glob
import pandas as pd
os.chdir("./cleanData")

extension = 'csv'
all_filenames = [i for i in glob.glob('passed_failed_*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, delimiter=";") for f in all_filenames ])
#export to csv
combined_csv.to_csv( "passed_failed_combined.csv", index=False)

print "done"