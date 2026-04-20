from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows the frontend to make requests

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/submit', methods=['POST'])
def handle_form():
    data = request.json
    # Process your data here (similar to your Assignment 2 logic)
    print(f"Received data: {data}")
    return jsonify({"status": "success", "message": "Data received by Flask!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)