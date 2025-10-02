from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

DUMMY_ID = "60d0fe4f5311236168a10a1b"

BASE_URL = "https://dummyapi.io/data/v1/"
HEADER = {"app-id":  DUMMY_ID}

@app.route("/user", methods=["GET"])
def get_users():
    url = f"{BASE_URL}/user"
    params = {
        "page":request.args.get("page", default=0, type=int),
        "limit": request.args.get("limit",default=10,type=int)
    }
    reponse = requests.get(url, headers=HEADER, params=params)
    return jsonify(reponse.json())