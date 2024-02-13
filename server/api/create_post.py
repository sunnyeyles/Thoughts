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


# def submit_post(image, post_body):
#     S3_BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"
#     # image_path = "/Users/sunnyeyles/Documents/projects/denny_sunny_todos/server/api/s3/IMG_3943.JPG"

#     if os.path.exists(image):
#         print("Image path exists")
#         with open(image, "rb") as image_file:
#             print("Opened image file")
#             image_filename = f"{uuid4()}.jpg"

#             # save the image temporarily on the server
#             with open(image_filename, "wb") as temp_image:
#                 print("Opened temp image file")
#                 temp_image.write(image_file.read())

#             print("Image saved temporarily")

#             # upload the image to S3 and save the path
#             s3.upload_file(image_filename, S3_BUCKET_NAME, image_filename)
#             image_url = f"https://why-are-there-so-many-bucket-naming-rules.s3.amazonaws.com/{image_filename}"

#             # save details to db
#             connection = sqlite3.connect("../../posts.db")
#             cursor = connection.cursor()
#             post_body = post_body
#             cursor.execute(
#                 "INSERT INTO posts (post_body, image_url) VALUES (?, ?)",
#                 (post_body, image_url),
#             )
#             connection.commit()
#             connection.close()
#             os.remove(image_filename)


#     return "Post submitted successfully"
def submit_post(image_path, post_body):
    S3_BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"

    if image_path:
        print("Image path exists")
        with open(image_path, "rb") as image_file:
            print("Opened image file")
            image_filename = f"{uuid4()}.jpg"

            # upload the image to S3 and save the path
            s3.upload_file(image_path, S3_BUCKET_NAME, image_filename)
            image_url = f"https://why-are-there-so-many-bucket-naming-rules.s3.amazonaws.com/{image_filename}"

            # save details to db
            db_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "../database/posts.db")
            )
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO posts (post_body, image_url) VALUES (?, ?)",
                (post_body, image_url),
            )
            connection.commit()
            connection.close()

            # Remove the temporary image file
            os.remove(image_path)

        return "Post submitted successfully"
    else:
        return "Image path not provided"
