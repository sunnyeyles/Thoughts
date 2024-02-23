import os
from dotenv import load_dotenv
import boto3
from uuid import uuid4
import sqlite3
from flask import request

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


# create and handle new post

def submit_post(image_path, post_body, user_id):
    S3_BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"  
    
    
    if image_path:
        with open(image_path, "rb") as image_file:
            
            # give image a unique name
            image_filename = f"{uuid4()}.jpg"
            
            
            # upload the image to S3 and save the path
            s3.upload_file(image_path, S3_BUCKET_NAME, image_filename)
            image_url = f"https://why-are-there-so-many-bucket-naming-rules.s3.amazonaws.com/{image_filename}"
            print(image_url)
            
            
            # save details to db
            db_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../database/posts.db")
            )
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO posts (post_body, image_url, user_id) VALUES (?, ?, ?)",
                (post_body, image_url, user_id),
            )
            connection.commit()
            connection.close()
            

            # Remove the temporary image file
            os.remove(image_path)
    
        return "Post submitted successfully"
    else:
        return "Image path not provided"
    
    