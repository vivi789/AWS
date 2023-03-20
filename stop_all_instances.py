import boto3
region = "us-east-1"
ec2 = boto3.resource('ec2', region_name=region)
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values':['running']}]
)

# stop each instance
def lambda_handler(event, context):
    for instance in instances:
        instance.stop()
        print(f"Instance {instance.id} has been stopped")
