import boto3 as bt

ec2 = bt.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-080e1f13689e07408',  # Ubuntu Server 20.04 LTS (HVM) Change as per your AMI
    MinCount=1,
    MaxCount=int(input("Enter the maximum number of instances to be launched : ")), 
    InstanceType='t2.micro',  # Change as per your instance type
    KeyName='ubuntu-instance'  # Change as per your key pair
)

print(instances + " instances are launched successfully")