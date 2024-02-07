# routes.py
from flask import jsonify, request
from .apis import  get_user_by_id, add_user, add_post_to_database

def configure_routes(app):
    
    # get all data from db
    @app.route("/api/get_all", methods=["GET"])
    def get_home():
        return {"message": "Yo whatup, it's flask"}
    
    
    # create new post
    @app.route("/api/new-post", methods=["POST"])
    def new_post():
        data = request.get_json()
        print("Looks like json but it's a dictionary",data)
        # add_post_to_database(post_data)
        return "Post Added successfully", 201


    # get user by id
    @app.route("/api/get-user/<user_id>", methods=["GET"])
    def get_user_by_id():
        user_id = request.args.get('user_id', type=int)
        records = get_record_by_year(year)
        return jsonify({'gta_records': records})



    
    
