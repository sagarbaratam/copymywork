import json
import boto3
dict={}
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    image = ec2.Image('id')
    for instance in ec2.instances.all():
        dict[instance.id]=instance.image.id
    for key in dict:
        response = client.describe_images(ImageIds=[dict[key]])
        for ami in response['Images']:
            if ami['BlockDeviceMappings'][0]['Ebs']['Encrypted'] != "false":
                 client.stop_instances(InstanceIds=[key])
                 
        
    return
