# routes.py
from flask import jsonify, request
from .apis import get_user_by_id, add_user, get_all_posts_from_db
from .create_post import submit_post
from werkzeug.utils import secure_filename
import os
import json


# from .create_post import create_post


def configure_routes(app):
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
        
        post_body = request.form.get("post")
        image_file = request.files.get("file")
        user_id = request.form.get("userId")
   
        image_path = "./files" + secure_filename(image_file.filename)
        image_file.save(image_path)
        submit_post(image_path, post_body, user_id)

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
    
    @app.route("/api/get-all-posts", methods=["GET"])
    def get_all_posts():
        all_posts = get_all_posts_from_db()
        
        return all_posts
        
    
