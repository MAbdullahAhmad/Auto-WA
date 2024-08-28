import requests

class WhatsAppExtensionManager:
    
    @staticmethod
    def get_unread_messages():

        base_url="http://localhost:5000"

        try:
            response = requests.get(f"{base_url}/get_messages")
            if response.status_code == 200:
                return response.json().get('new_messages')
            return []
        except Exception as e:
            print(f"Error in get_unread_messages: {e}")
            return []