import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    client = boto3.client("ec2")
    s3 = boto3.client("s3")
    status = client.describe_instance_status(IncludeAllInstances= True)
    #with open("/tmp/log.txt","w") as f:
    #    json.dump(status, f)
    #s3.upload_file("/tmp/log.txt","harspbucket","logs.txt")
    
    s3.put_object(Bucket="harspbucket", Key="data-logs.txt", Body=str(status))
    
    #pprint(status)
    for i in status["InstanceStatuses"]:
        print("AvailabilityZone :", i["AvailabilityZone"])
        print("InstanceId :", i["InstanceId"])
        print("InstanceState :", i["InstanceState"])
        print("InstanceStatus :", i["InstanceStatus"])
        print("SystemStatus: ", i["SystemStatus"])
        print("\n")
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

