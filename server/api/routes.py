# routes.py
from flask import jsonify, request
from .apis import get_user_by_id, add_user, add_post_to_database, get_post_from_db
from .create_post import submit_post
from werkzeug.utils import secure_filename
import os
import json


# from .create_post import create_post


def configure_routes(app):
    # get all data from db
    @app.route("/api/get_all", methods=["GET"])
    def get_home():
        return {"message": "Yo whatup, it's flask"}

    # create new post
    @app.route("/api/new-post", methods=["POST"])
    def new_post():
        data = request.args.get("id")

        # add_post_to_database(post_data)
        return "Post Added successfully", 201

    # get user by id
    @app.route("/api/get-user/<user_id>", methods=["GET"])
    def get_user_by_id():
        user_id = request.args.get("user_id", type=int)
        records = get_record_by_year(year)
        return jsonify({"gta_records": records})

    @app.route("/api/get-post-by-id", methods=["GET"])
    def get_post_by_id():
        post_id = request.args.get("id")
        post = get_post_from_db(post_id)
        if post:
            return jsonify({"message": post})
        else:
            return jsonify({"error": "Post not found"}), 404

    # CREATE NEW POST

    @app.route("/api/create-post", methods=["POST"])
    def create_new_post():

        post_data = request.form.get("post")
        image_file = request.files.get("imageFile")
        image_path = "./files" + secure_filename(image_file.filename)
        image_file.save(image_path)
        submit_post(image_path, post_data)

        if image_file:
            return (
                jsonify(
                    {
                        "message": "Image uploaded successfully",
                    }
                ),
                200,
            )
        else:
            return jsonify({"error": "Image not found in the request"}), 400
