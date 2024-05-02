import boto3
commands = [' echo "hello world"']
ssm_client = boto3.client('ssm')

output = ssm_client.send_command(
InstanceIds=[""], # replace with your instance id
DocumentName="AWS-RunShellScript", # Document name
Parameters={
    'commands': commands # Command
    }
)

# Dont forget to replace the instance id with your instance id
# Dont forgot to enable the SSM service in your instance