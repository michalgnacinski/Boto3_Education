import os
import sys
from xml.parsers import expat

import boto3
from botocore.exceptions import ClientError
import dotenv
from dotenv import load_dotenv

load_dotenv()
# Output of every ec2 on aws account
ec2 = boto3.client('ec2', region_name='eu-west-2')
response = ec2.describe_instances()
print(response)
# for reservation in response['Reservations']:
#     for instance in reservation['Instances']:
#         print(f"ID: {instance['InstanceId']}")
#         print(f"Nazwa: {instance['InstanceName']}")
#         print(f"Typ: {instance['InstanceType']}")
#         print(f"Status: {instance['State']['Name']}")
#         print('-' * 30)


#Start or Stop ec2 instance
# Running command: python ec2_practise.py <INSTANCE_ID> <ON/OFF>
# instance_id = sys.argv[1]
# action = sys.argv[2].upper()
#
# if action == 'ON':
#     try:
#         ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#     try:
#         response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)
# else:
#     try:
#         ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
#     except ClientError as e:
#         if 'DryRunOperation' not in str(e):
#             raise
#     try:
#         response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
#         print(response)
#     except ClientError as e:
#         print(e)

#Reboot instance
# INSTANCE_ID = os.getenv('INSTANCE_ID')
#
# try:
#     ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=True)
# except ClientError as e:
#     if 'DryRunOperation' not in str(e):
#         print("You dont have permissions to reboot this instance")
#         raise
#
# try:
#     response = ec2.reboot_instances(InstanceIds=[INSTANCE_ID], DryRun=False)
#     print('Succes', response)
# except ClientError as e:
#     print(e)




