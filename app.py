from flask import Flask, jsonify
from flask_cors import CORS  # Enable CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/')
def home():
    return "LA Museums API is running!"

@app.route('/exhibitions', methods=['GET'])
def get_exhibitions():
    # Simple test data to check if the API works
    exhibitions = [
        {"museum": "Hammer Museum", "title": "Sample Exhibition", "url": "https://hammer.ucla.edu/"},
        {"museum": "LACMA", "title": "Another Exhibition", "url": "https://www.lacma.org/"},
        {"museum": "Getty Museum", "title": "Getty Exhibition", "url": "https://www.getty.edu/"}
    ]
    return jsonify(exhibitions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
