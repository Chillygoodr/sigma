from flask import Flask, request, jsonify

api = Flask(__name__)

@api.route("/", methods=["GET"])
def home():
  return jsonify({"BlackFuckingMonkey": "1"})
@api.route("/Client/GetUserInventory", methods=["POST","GET"])
def ClientGetUserInventory():
    return jsonify({"BlackFuckingMonkey": "1"})

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8080)
