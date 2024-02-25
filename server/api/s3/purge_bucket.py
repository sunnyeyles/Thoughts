import os
from dotenv import load_dotenv
import boto3
from uuid import uuid4
import sqlite3

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
S3_BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"  

def purge_bucket():
    # print(s3.list_objects(Bucket=S3_BUCKET_NAME))
    all_objects = s3.list_objects(Bucket=S3_BUCKET_NAME)
    first_item_key, first_item_value = next(iter(all_objects.items()))
    for object in all_objects:
        # print(object)
        first_item_key, first_item_value = next(iter(object.items()))
        
        print(first_item_key, first_item_value)
        
    # request_id = all_objects['ResponseMetadata']['RequestId']




    
if __name__ == "__main__":
    purge_bucket()