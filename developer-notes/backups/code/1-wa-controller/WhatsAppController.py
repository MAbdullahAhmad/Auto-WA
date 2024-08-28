import pygetwindow as gw
import pyautogui
from time import sleep

from views.show_error import show_error
from managers.WhatsAppExtensionManager import WhatsAppExtensionManager

class WhatsAppController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.scanned = False

    def scan(self, main_window):
        # Check if WhatsApp is open in a browser window
        windows = gw.getWindowsWithTitle('WhatsApp Web')
        if windows:
            whatsapp_window = windows[0]
            whatsapp_window.activate()
            whatsapp_window.maximize()
            sleep(1)  # Give some time for the window to be activated

            # Here we would read the username from the WhatsApp window
            # This is a placeholder; actual implementation will depend on how you extract text
            # username = self.extract_username_from_window(whatsapp_window)

            # # Display username in MainWindow
            # self.main_window.set_username(username)

            # Set scanned to true
            self.scanned = True
        else:
            # Show error alert if WhatsApp window is not found
            show_error("WhatsApp window not found")

    def start(self):
        # Check if scan has been done
        if not self.scanned:
            show_error("Please Scan first")
            return

        # Keep checking for new messages
        while True:
            new_message = self.check_for_new_message()
            if new_message:
                self.main_window.set_input(new_message)
            sleep(1)  # Wait a bit before checking again

    # def extract_username_from_window(self, window):
    #     # Placeholder function to extract username from the window
    #     # This could be done using OCR, or by reading the content of the window somehow
    #     return "John Doe"

    def check_for_new_message(self):
        return WhatsAppExtensionManager
        # Placeholder function to check for new messages in WhatsApp
        # This might involve reading a specific part of the screen using OCR or automation tools
        return None  # Replace with actua
