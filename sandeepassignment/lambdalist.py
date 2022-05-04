import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('lambda')
    badfunctions= client.list_functions()
    jsondata=badfunctions["Functions"]
    list1 = []
    for i in jsondata:
        if 'VpcConfig' not in i:
            list1.append(i['FunctionName'])
    for i in list1:
        response = client.put_function_concurrency(FunctionName= i,ReservedConcurrentExecutions=0)
    return response
