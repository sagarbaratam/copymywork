import json
import boto3


def lambda_handler(event, context):
    client = boto3.client('lambda')
    badfunctions= client.list_functions()  ####Lists all functions as json objects####
    jsondata=badfunctions["Functions"]  #### Filtering json object to remove other info from json outPut and list only function related info####
    list1 = []
    for i in jsondata:
        if 'VpcConfig' not in i:     
            list1.append(i['FunctionName'])   ####Used indexing to get the function name from the entire function related info..####
    for i in list1:
        response = client.put_function_concurrency(FunctionName= i,ReservedConcurrentExecutions=0)  ####Throttle the bad fucntions and make them unexecutable####
    return response
