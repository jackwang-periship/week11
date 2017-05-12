'''
Created on May 10, 2017

@author: jwang02
'''
import sys
import boto3


ec2 = boto3.resource('ec2')
for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response
