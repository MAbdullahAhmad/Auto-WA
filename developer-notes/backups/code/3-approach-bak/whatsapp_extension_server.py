from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# The local port where the Chrome extension communicates
CHROME_EXTENSION_PORT = "5000"

@app.route('/get_username', methods=['GET'])
def get_username():
    try:
        # Request the username from the Chrome extension
        response = requests.post(f'http://localhost:{CHROME_EXTENSION_PORT}/extension', json={"action": "get_username"})
        if response.status_code == 200:
            return jsonify(username=response.json().get('username', 'Unknown'))
        else:
            return jsonify(username="Error retrieving username"), 500
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/get_unread_messages', methods=['GET'])
def get_unread_messages():
    try:
        # Request unread messages from the Chrome extension
        response = requests.post(f'http://localhost:{CHROME_EXTENSION_PORT}/extension', json={"action": "get_unread_messages"})
        if response.status_code == 200:
            return jsonify(messages=response.json().get('messages', []))
        else:
            return jsonify(messages=[]), 500
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get("message", "")
    try:
        # Request to send a message via the Chrome extension
        response = requests.post(f'http://localhost:{CHROME_EXTENSION_PORT}/extension', json={"action": "send_message", "message": message})
        if response.status_code == 200:
            return jsonify(success=response.json().get('success', False))
        else:
            return jsonify(success=False), 500
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(port=5001)
