from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/data")
def get_data():
    return {"message": "Yo whatup, it's flask"}
    
if __name__ == "__main__":
    app.run(debug=True)
