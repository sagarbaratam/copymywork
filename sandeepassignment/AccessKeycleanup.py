import json
import boto3
from datetime import datetime
from datetime import timedelta
from botocore.exceptions import ClientError
list_users_to_remove = []
list_access_keys_to_remove = []
date_now = datetime.now() + timedelta(days=30)
iam_client = boto3.client('iam')
max_idle_days = 30
max_items = 50



def lambda_handler(event, context):
    created_date = datetime.now()
    last_used_date = datetime.now()
    access_key_id = None
    res_users = iam_client.list_users(MaxItems=max_items)
    for user in res_users['Users']:
        res_keys = iam_client.list_access_keys(UserName=user['UserName'])
        if 'AccessKeyMetadata' in res_keys:
                for key in res_keys['AccessKeyMetadata']:
                    if 'CreateDate' in key:
                        created_date = res_keys['AccessKeyMetadata'][0]['CreateDate'].replace(tzinfo=None)
                    if 'AccessKeyId' in key:
                        access_key_id = key['AccessKeyId']
                        res_last_used_key = iam_client.get_access_key_last_used(AccessKeyId=access_key_id)
                        if 'LastUsedDate' in res_last_used_key:
                            last_used_date = res_last_used_key['AccessKeyLastUsed']['LastUsedDate'].replace(tzinfo=None)
                    else:
                        last_used_date=created_date
                    difference = date_now - last_used_date
                    if difference.days > max_idle_days:
                        list_access_keys_to_remove.append(access_key_id)
                    
                for access_key_id in list_access_keys_to_remove:
                    print('Access key {0} needs to be removed'.format(access_key_id))
                    iam_client.delete_access_key(AccessKeyId= access_key_id)

    return 
