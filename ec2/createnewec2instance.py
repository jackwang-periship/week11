'''
Created on May 10, 2017

@author: jwang02
'''
import boto3


ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-618fab04',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print instance[0].id