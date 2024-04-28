import boto3

# Create IAM client
iam = boto3.client('iam')

# Create user
iam.create_user(
    UserName='aws-python-user',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'aws-python-user'
        },
    ]
)

# Attach a policy
iam.attach_user_policy(
    UserName='aws-python-user',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)