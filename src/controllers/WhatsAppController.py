import subprocess
from time import sleep

from views.show_error import show_error
from managers.XDoToolManager import XDoToolManager
from managers.WhatsappExtensionManager import WhatsAppExtensionManager
from .TextGenerationController import TextGenerationController
from PyQt5.QtWidgets import QApplication

scanned = False

class WhatsAppController:

    @staticmethod
    def scan(main_window):
        global scanned

        print("Scanning")
        # Find WhatsApp window using wmctrl
        try:
            result = subprocess.run(['wmctrl', '-l'], capture_output=True, text=True)
            windows = result.stdout.splitlines()

            whatsapp_window = None
            for window in windows:
                if "WhatsApp" in window:
                    whatsapp_window = window.split()[0]
                    break

            if whatsapp_window:
                # Activate the window using wmctrl
                subprocess.run(['wmctrl', '-i', '-a', whatsapp_window])
                sleep(1)  # Give time for the window to be activated

                # # Placeholder to extract username - implement this based on your needs
                # username = WhatsAppController.extract_username_from_window()

                # # # Display username in MainWindow
                # # main_window.set_username(username)
                # print(username)

                # Set scanned to true
                scanned = True
            else:
                # Show error alert if WhatsApp window is not found
                show_error("WhatsApp window not found")
        except Exception as e:
            show_error(f"Error occurred: {str(e)}")

    @staticmethod
    def start(main_window):
        global scanned

        # Check if scan has been done
        if not scanned:
            show_error("Please Scan first")
            return

        # Keep checking for new messages
        while True:
            new_messages = WhatsAppExtensionManager.get_unread_messages()
            if new_messages:
                for message in new_messages:
                    main_window.set_input(message)
                    TextGenerationController.generate(main_window)
                    QApplication.processEvents()
                    WhatsAppController.send_message(main_window)

            QApplication.processEvents()
            sleep(1)

    @staticmethod
    def send_message(main_window):
        XDoToolManager.send_message(
            main_window.get_output()
        )

    # @staticmethod
    # def extract_username_from_window():
    #     # Placeholder function to extract username
    #     return "John Doe"

    # @staticmethod
    # def check_for_new_message():
    #     # Placeholder function to check for new messages in WhatsApp
    #     return None  # Replace with actual message if found

