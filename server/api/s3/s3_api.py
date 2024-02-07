from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

@app.route('/users', methods=['GET'])
def get_users():
    # Query all users from the database
    users = User.query.all()

    # Serialize the user data into JSON
    user_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    # Return the serialized user data as a JSON response
    return jsonify(users=user_data)

if __name__ == '__main__':
    app.run(debug=True)
