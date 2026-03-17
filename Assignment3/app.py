from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

app = Flask(__name__)

# MongoDB Atlas connection - will be initialized when needed
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

def get_db():
    client = MongoClient(MONGO_URI)
    return client[DB_NAME]
# @app.route('/')
# def home():
#     return "Hello, World! This is the home page of the Flask app."

@app.route('/api')
def api():
    with open('data.txt', 'r') as data:
       # Strip removes the newline character (\n) from each line
        items = [line.strip() for line in data.readlines()]
    return jsonify(items)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Insert into MongoDB
        data = {
            'name': name,
            'email': email,
            'message': message
        }
        db = get_db()
        collection = db[COLLECTION_NAME]
        collection.insert_one(data)
        
        # Redirect to success page
        return redirect(url_for('success'))
    except Exception as e:
        # On error, render homepage with error
        return render_template('homepage.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)