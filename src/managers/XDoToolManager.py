import os

class XDoToolManager:

    @staticmethod
    def send_message(text):
        # Coordinates for the mouse click
        x = 1050
        y = 1002

        # Move the mouse to the specified coordinates and click
        os.system(f"xdotool mousemove {x} {y} click 1")

        # Escape single quotes in the text
        escaped_text = text.replace('\"', "\\\"")

        # Type the text using xdotool
        os.system(f"xdotool type \"{escaped_text}\"")

        # Press Enter to send the text
        os.system("xdotool key Return")

