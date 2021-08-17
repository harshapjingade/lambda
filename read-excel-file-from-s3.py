import json
import pandas as pd
import boto3
import io


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    if event:
        s3_records = event["Records"][0]
        bucket_name = str(s3_records["s3"]["bucket"]["name"])
        file_name = str(s3_records["s3"]["object"]["key"])
        file_obj = s3.get_object(Bucket=bucket_name,Key=file_name)
        
        file_content = file_obj["Body"].read()
        read_excel_data = io.BytesIO(file_content)
        
        df = pd.read_excel(read_excel_data)
	df = df.assign(dummy="dummy_value")
	df.to_csv("/tmp/updated.csv")
	
	s3_resource = boto3.resource("s3")
	s3_resource.Bucket("harspbucket").upload_file("/tmp/updated.csv","updated.csv")
        
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
