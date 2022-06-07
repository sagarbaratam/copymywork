import json
import boto3

elb = boto3.client('elbv2')
   
#----This Function lists all the ALB's-----#
def listalbarn():
    lbs = elb.describe_load_balancers()
    arn=[i['LoadBalancerArn'] for i in lbs['LoadBalancers']]
    return arn
  
#-----This Function Creates a dictonary of loadbalancers as keys and targetgroups as values-------------#
def targetgrparn():
    tgarns={}
    for arn in listalbarn():
        tgs=elb.describe_target_groups(LoadBalancerArn=arn)
        for tg in tgs["TargetGroups"]:
            try:
                tgarns[arn].append(tg['TargetGroupArn'])
            except KeyError:
                tgarns[arn]=[tg['TargetGroupArn']]
                
    return tgarns
  
#----This Function lists all the ALB without any targetgroups-----#    
 
def getemptyalb():
    Emptyalb= listalbarn()
    for arn in listalbarn():
        tgs=elb.describe_target_groups(LoadBalancerArn=arn)
        if 'TargetGroups' in tgs:
            for tg in tgs['TargetGroups']:
                if arn in Emptyalb:
                    Emptyalb.remove(arn)
                    
    return Emptyalb
  
#-----This Function Lists load balancers with Empty targetgroups-----#
    
def getemptytargetgrp():
    Emptytargetgrp= targetgrparn()
    for key,value in targetgrparn().items():
        for i in value:
            tg=elb.describe_target_health(TargetGroupArn=i)
            for t in tg['TargetHealthDescriptions']:
                if 'Target' in t:
                    del Emptytargetgrp[key]
                    print(list(Emptytargetgrp.keys()))
                
    return list(Emptytargetgrp.keys())
#---This Function Lists and deletes all unwanted loadbalancers---#              
def deletebadalb():
    list1=getemptyalb()+getemptytargetgrp()
    print(list1)
    for i in list1:
        print(i)
        #elb.delete_load_balancer(LoadBalancerArn=i)
    return
    
def lambda_handler(event, context):
  
    return deletebadalb()
