import os
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

local_file_path = (
    "/Users/sunnyeyles/Documents/projects/denny_sunny_todos/server/api/s3/IMG_3943.JPG"
)
bucket_name = "why-are-there-so-many-bucket-naming-rules"

# s3 key is the path to where the file will be stored in the S3 bucket
# we might want to add an id to the end of the file name to make it unique
s3_key = "images/IMG_3943.JPG"


try:
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f"File uploaded successfully to S3 bucket {bucket_name} with key {s3_key}")
except Exception as e:
    print(f"Error uploading file to S3: {e}")
