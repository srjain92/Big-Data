import boto3
from botocore.client import Config
import os

ACCESS_KEY_ID = "Access Key"
ACCESS_SECRET_KEY = "Secret Key"
BUCKET_NAME = "sj-databricks"

data = open("C:\\Users\\Saurabh.Jain\\Desktop\\Amazon.csv", 'rb')
# path = "C:\\Users\\Saurabh.Jain\\Desktop\\Resume"

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key="Practice", Body=data)

# for filename in os.listdir(path):
#     data = path + "\\" + filename
#     s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)


print("Done")
