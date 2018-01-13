# #############
# AWS EC2 Class
# -------------------------------
# @Github: https://github.com/gnubyte
# @Author: Patrick Hastings
# @AppVersion: 0.1
# @PythonVersion: 3.6.x
# @Purpose: implements AWS SDK to allow us to abstract
# -------------------------------
# - 01/11/18 PH: resources here are many, need to expand out to a ec2 manager now (great!)
# #############
import boto3
from pprint import pprint

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    #print(repr(instance)) #stackdatas short...print dict if avail as single string rep
    #pprint (vars(instance)) # need this instance's attributes....
    print (instance.id, instance.state, instance.tags)

#instance_id = sys.argv[2]


#NewSH = ec2.create_instances(
#    ImageId='ami-f2ce648a',
#    MinCount=1,
#    MaxCount=1,
#    InstanceType='t2.micro')
# leaving out tags....Proof of concept first
#print (NewSH[0].id)
response = ec2.start_instances(DryRun=False)
print (response)
# InstanceIds=[instance_id], 
class awsEC2:
    '''a singular EC2 instance object'''
    
    def retrieve_instance(self, **kwargs):
        '''retrieves single EC2 instance from AWS and sets it'''
        result = {
            'a': lambda x: x * 5,
          'b': lambda x: x + 7,
          'c': lambda x: x - 2
        }[value](x)
        