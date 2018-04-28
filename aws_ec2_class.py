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
#for instance in ec2.instances.all():
    #print(repr(instance)) #stackdatas short...print dict if avail as single string rep
    #pprint (vars(instance)) # need this instance's attributes....
#    print (instance.id, instance.state, instance.tags)

#instance_id = sys.argv[2]


NewSH = ec2.create_instances(
    ImageId='ami-f2ce648a',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
# leaving out tags....Proof of concept first
ec2.create_tags(DryRun=False,
                Resources=[NewSH[0].id],
                Tags=[{'Key':'Name',
                       'Value':'PH-StopTestAutoCloud-IDX-01'},
                      {'Key': 'Owner',
                       'Value':'Patrick Hastings'},
                      {'Key':'Date',
                       'Value':'01-16-2018 9:01PM EST'}])



print (NewSH[0].id)
response = ec2.start_instances(DryRun=False)
print (response)
# InstanceIds=[instance_id], 

