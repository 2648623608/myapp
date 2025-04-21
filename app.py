from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['POST'])
def getRes():
    data = request.get_json()
    input_text = data.get('sendtext')

    # 确保有输入的文本
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400

    # 外部 API 地址
    url = "http://117.50.33.172:8000/"
    headers = {
        "Content-Type": "application/json",  # 如果外部API需要JSON格式的请求体
    }

    # 请求的 payload
    payload = {
        "sendtext": input_text
    }

    try:
        # 发送 POST 请求
        response = requests.post(url, json=payload, headers=headers)

        # 检查外部请求是否成功
        if response.status_code == 200:
            return jsonify({"response": response.json()}), 200  # 假设返回的是JSON数据
        else:
            return jsonify({"error": f"API request failed with status code {response.status_code}"}), 500
    except requests.exceptions.RequestException as e:
        # 处理请求错误
        return jsonify({"error": f"Request to external API failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
