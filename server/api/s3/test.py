import os
from dotenv import load_dotenv
import boto3
from uuid import uuid4
import sqlite3

name = "main"

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

# List all buckets
if __name__ == "__main__":
    buckets_resp = s3.list_buckets()
    for bucket in buckets_resp["Buckets"]:
        print(bucket)