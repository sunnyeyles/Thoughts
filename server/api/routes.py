# routes.py
from flask import jsonify, request
from .apis import  get_record_by_year, add_user, add_post_to_database

def configure_routes(app):
    
    # get all data from db
    @app.route("/api/get_all", methods=["GET"])
    def get_home():
        return {"message": "Yo whatup, it's flask"}
    

    
    @app.route("/api/by-year", methods=["GET"])
    def get_data_by_year():
        year = request.args.get('year', type=int)
        if year is None:
            return jsonify({'error': 'Year parameter is missing or not valid'}), 400

        records = get_record_by_year(year)
        return jsonify({'gta_records': records})


    
    @app.route("/api/new-post", methods=["POST"])
    def new_post():
        post_data = request.json
        print(post_data)
        add_post_to_database(post_data)
        return "Post Added successfully", 201

    
    
