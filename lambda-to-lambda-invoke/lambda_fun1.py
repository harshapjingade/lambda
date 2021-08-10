import boto3, json
def lambda_handler(event, context):
    invokeLam = boto3.client("lambda", region_name="ap-south-1")
    payload = {"message": "Hi, you have been invoked."}

    resp = invokeLam.invoke(FunctionName = "lambda_fun2", InvocationType = "RequestResponse", Payload = json.dumps(payload))
    print(resp["Payload"].read())

    resp = invokeLam.invoke(FunctionName = "lambda_fun2", InvocationType = "Event", Payload = json.dumps(payload))
    return 'Thanks'
