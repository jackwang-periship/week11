'''
Created on May 10, 2017

@author: jwang02
'''
import sys
import boto3


db = sys.argv[1]
rds = boto3.client('rds')
try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db,
        SkipFinalSnapshot=True)
    print response
except Exception as error:
    print error


