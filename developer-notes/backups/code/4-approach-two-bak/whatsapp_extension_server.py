from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Global variables to store messages
new_messages = []
messages_to_send = []

@app.route('/sync', methods=['POST'])
def sync():
    global new_messages, messages_to_send
    data = request.get_json()

    # Add new messages received from the extension to new_messages list
    if 'new_messages' in data:
        new_messages.extend(data['new_messages'])

    # If there are messages to send, return them and clear the list
    if messages_to_send:
        message_to_send = messages_to_send.pop(0)
        return jsonify({"message_to_send": message_to_send})

    # Otherwise, just acknowledge the sync
    return jsonify({"message_to_send": None})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    global new_messages
    messages = new_messages
    new_messages = []  # Clear the list after sending
    return jsonify({"new_messages": messages})

@app.route('/send_message', methods=['POST'])
def send_message():
    global messages_to_send
    data = request.get_json()
    message = data.get("message", "")
    if message:
        messages_to_send.append(message)
        return jsonify({"success": True})
    return jsonify({"success": False}), 400

if __name__ == '__main__':
    app.run(port=5000)
