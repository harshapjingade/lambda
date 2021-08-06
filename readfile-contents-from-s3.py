import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucket_name = str(file_obj['s3']['bucket']['name'])
        file_name = str(file_obj['s3']['object']['key'])
        print("Filename: ", file_name)
        file_obj = s3.get_object(Bucket=bucket_name,Key=file_name)
        file_content = file_obj["Body"].read().decode('utf-8')
        print(file_content)
    return 'thanks'
