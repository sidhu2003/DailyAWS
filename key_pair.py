import boto3

ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='aws_key_pair')
print(response)