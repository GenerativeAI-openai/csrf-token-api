from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ CSRF Token API is running"

@app.route("/get-csrf-token")
def get_csrf_token():
    try:
        res = requests.get("https://playentry.org/")
        soup = BeautifulSoup(res.text, 'html.parser')
        tag = soup.select_one('meta[name="csrf-token"]')
        if tag:
            return jsonify({"csrf_token": tag['content']})
        else:
            return jsonify({"error": "CSRF token not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
