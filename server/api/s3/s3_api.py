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


# # @app.route("/submit-post")
# def submit_post():
#     # # Get message content from the request
#     # message_content = request.form.get("message_content")
#     # # Get image file from the request
#     # image_file = request.files.get("image")
#     image_file = "/Users/sunnyeyles/Documents/projects/denny_sunny_todos/server/api/s3/IMG_3943.JPG"

#     if image_file:
#         # create unique id for image
#         image_filename = f"{uuid4()}.jpg"

#         # Save the image temporarily on the server
#         image_file.save(image_filename)

#         # upload the image to S3 and save the path
#         s3.upload_file(image_filename, S3_BUCKET_NAME, image_filename)
#         image_url = f"https://why-are-there-so-many-bucket-naming-rules.s3.amazonaws.com/{image_filename}"

#         connection = sqlite3.connect("posts.db")
#         cursor = connection.cursor()
#         post_body = "OIIIIIIII"

#         cursor.exectute(
#             "INSERT INTO posts (post_body, image) VALUES (?, ?)", (post_body, image_url)
#         )
#         connection.commit()
#         connection.close()

#         # Remove the temporary image file
#         os.remove(image_filename)

#     return "Post submitted successfully"


# submit_post()
def submit_post():
    S3_BUCKET_NAME = "why-are-there-so-many-bucket-naming-rules"
    print("Inside submit_post function")
    image_path = "/Users/sunnyeyles/Documents/projects/denny_sunny_todos/server/api/s3/IMG_3943.JPG"

    if os.path.exists(image_path):
        print("Image path exists")
        with open(image_path, "rb") as image_file:
            print("Opened image file")
            # create unique id for image
            image_filename = f"{uuid4()}.jpg"

            # Save the image temporarily on the server
            with open(image_filename, "wb") as temp_image:
                print("Opened temp image file")
                temp_image.write(image_file.read())

            print("Image saved temporarily")

            # upload the image to S3 and save the path
            s3.upload_file(image_filename, S3_BUCKET_NAME, image_filename)
            image_url = f"https://why-are-there-so-many-bucket-naming-rules.s3.amazonaws.com/{image_filename}"

            print("Image uploaded to S3")

            connection = sqlite3.connect("../../posts.db")
            cursor = connection.cursor()
            post_body = "OIIIIIIII"

            cursor.execute(
                "INSERT INTO posts (post_body, image_url) VALUES (?, ?)",
                (post_body, image_url),
            )
            connection.commit()
            connection.close()

            print("Data inserted into database")

            # Remove the temporary image file
            os.remove(image_filename)

            print("Temporary image file removed")

    return "Post submitted successfully"


if __name__ == "__main__":
    submit_post()
