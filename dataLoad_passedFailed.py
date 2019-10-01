__author__ = "Johan Louwers"
__copyright__ = "Copyright 2019, Johan Louwers"
__license__ = "MIT"
__email__ = "louwersj@gmail.com"

''' 
    This example code is a private example code and comes as-is without any warranty under the mentioned license.

    The intention of this code is to load the cleaned and merged passed_failed data into an Oracle Autonomous Data 
    Warehouse by leveraging the .to_sql functionality from Pandas. 
    
    DO NOTE:
    The data, as it will be loaded is not normalized at this moment. Main reason for this is that it is not known what 
    role the data will play for the user. In cases where the user wants to experiment with a flat (none normalized) data
    table this load solution can be used in isolation. In case the data needs to be loaded / transformed into a more 
    normalized data model there is a need to for a normalize SQL script which can do so. (this is not part of this 
    specific python script)
'''


## WARNING -- Currently in development -- DO NOT USE

import pandas as pd
import cx_Oracle as cxo

# change the below values when needed.
sourceFileName = "./cleanData/passed_failed_combined.csv"
conn_str = u'account/password@host:1521/server'
#conn = cxo.connect(conn_str)


data = pd.read_csv(sourceFileName)

print(data.head())

