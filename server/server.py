# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from server.routes.apis import get_all_gta_records
# from server.routes.apis import get_record_by_year
# from server.routes.apis import add_user

# app = Flask(__name__)
# CORS(app)



# @app.route("/api/data", methods=["GET"])
# def get_home():
#     return {"message": "Yo whatup, it's flask"}
    
# @app.route("/api/gta",methods=["GET"])
# def get_data():
#     return get_all_gta_records()
    
    
# @app.route("/api/by-year",methods=["GET"])
# def get_data_by_year():
#     year = request.args.get('year', type=int)
#     if year is None:
#         return jsonify({'error': 'Year parameter is missing or not valid'}), 400

#     records = get_record_by_year(year)
#     return jsonify({'gta_records': records})
    

# @app.route("/api/add-user", methods=["POST"])
# def new_user():
#     user = request.json
#     add_user(user)
#     return "User added successfully", 201


# if __name__ == "__main__": 
#     app.run(debug=True)
# server.py
from flask import Flask
from flask_cors import CORS
from server.routes import configure_routes

app = Flask(__name__)
CORS(app)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
