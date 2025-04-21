from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/', methods=['POST'])
def getRes():
    data = request.get_json()
    input_text = data.get('sendtext')
    url = "http://117.50.33.172:8000/"
    params = {
        "sendtext": input_text
    }
    response = requests.get(url, params=params)
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
