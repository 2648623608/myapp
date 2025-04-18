from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getRes():
    input_text = request.args.get('sendtext')
    url = "http://117.50.33.172:8000/"
    params = {
        "sendtext": input_text
    }
    response = requests.get(url, params=params)
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
