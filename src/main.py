from views.MainWindow import start_main_window, main_window

from controllers.TextGenerationController import TextGenerationController
from controllers.WhatsAppController import WhatsAppController

if __name__ == "__main__":
    
    main_window.on_generate_click(TextGenerationController.generate)
    main_window.on_scan_click(WhatsAppController.scan)
    main_window.on_send_click(WhatsAppController.send_message)
    main_window.on_start_click(WhatsAppController.start)

    start_main_window() 
