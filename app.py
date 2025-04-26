from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['POST'])
def getRes():
    data = request.get_json()
    input_text = data.get('sendtext')

    if not input_text:
        return jsonify({"error": "No input text provided"}), 400

    url = "http://117.50.33.172:8000/"
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "sendtext": input_text
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return jsonify({"response": response.json()}), 200 
        else:
            return jsonify({"error": f"API request failed with status code {response.status_code}"}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request to external API failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
