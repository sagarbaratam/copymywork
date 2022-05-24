import json
import boto3
dict={}
unencrypted=[]
def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    image = ec2.Image('id')
    for instance in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]):
        dict[instance.id]=instance.image.id
        for key in dict:
            response = client.describe_images(ImageIds=[dict[key]])
            for ami in response['Images']:
                if ami['BlockDeviceMappings'][0]['Ebs']['Encrypted'] != "false":
                    unencrypted.append(key)
        
        for inst in unencrypted:
             print('Instance {0} needs to be removed'.format(inst))
             client.stop_instances(InstanceIds=[inst])
    
                 
        
    return 
