import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    
    def __init__(self):

        # Placeholder functions
        self._start_callback = None
        self._generate_callback = None
        self._copy_callback = None
        self._scan_callback = None
        self._send_callback = None

        super().__init__()

        # Window setup
        self.setWindowTitle("Auto-WA")
        self.setGeometry(100, 100, 600, 400)

        # Set the window to always be on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Create left and right sections
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Buttons on the left
        self.scan_button = QPushButton("Scan", self)
        self.start_button = QPushButton("Start", self)
        self.generate_button = QPushButton("Generate", self)
        self.copy_button = QPushButton("Copy", self)
        self.send_button = QPushButton("Send", self)

        left_layout.addWidget(self.scan_button)
        left_layout.addWidget(self.start_button)

        # Input and output areas on the right
        self.input_area = QLineEdit(self)
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)

        right_layout.addWidget(self.input_area)
        right_layout.addWidget(self.generate_button)
        right_layout.addWidget(self.output_area)
        right_layout.addWidget(self.copy_button)
        right_layout.addWidget(self.send_button)

        # Horizontal layout for left and right sections
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addLayout(left_layout, 1)
        horizontal_layout.addLayout(right_layout, 3)

        # Add the horizontal layout to the main layout
        main_layout.addLayout(horizontal_layout)

        # Status bar with LEDs
        self.status_bar = QHBoxLayout()
        self.green_led = QLabel("●", self)
        self.green_led.setStyleSheet("color: gray; font-size: 18px;")
        self.red_led = QLabel("●", self)
        self.red_led.setStyleSheet("color: gray; font-size: 18px;")

        self.status_bar.addWidget(QLabel("Status:", self))
        self.status_bar.addWidget(self.green_led)
        self.status_bar.addWidget(self.red_led)
        main_layout.addLayout(self.status_bar)

        # Connect buttons to their methods
        self.scan_button.clicked.connect(self.handle_scan_click)
        self.start_button.clicked.connect(self.handle_start_click)
        self.generate_button.clicked.connect(self.handle_generate_click)
        self.copy_button.clicked.connect(self.handle_copy_click)
        self.send_button.clicked.connect(self.handle_send_click)

        # Set initial window size
        self.resize(500, 500)

    def set_status_led(self, color):
        if color == 'green':
            self.green_led.setStyleSheet("color: green; font-size: 18px;")
            QTimer.singleShot(200, lambda: self.green_led.setStyleSheet("color: gray; font-size: 18px;"))
        elif color == 'red':
            self.red_led.setStyleSheet("color: red; font-size: 18px;")
            QTimer.singleShot(200, lambda: self.red_led.setStyleSheet("color: gray; font-size: 18px;"))


    def handle_start_click(self):
        if self._start_callback:
            self._start_callback(self)

    def handle_generate_click(self):
        if self._generate_callback:
            self._generate_callback(self)

    def handle_copy_click(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_area.toPlainText())
        self.set_status_led("green")

    def handle_scan_click(self):
        if self._scan_callback:
            self._scan_callback(self)

    def handle_send_click(self):
        if self._send_callback:
            self._send_callback(self)


    def on_start_click(self, func):
        self._start_callback = func

    def on_generate_click(self, func):
        self._generate_callback = func

    def on_scan_click(self, func):
        self._scan_callback = func

    def on_send_click(self, func):
        self._send_callback = func


    def set_input(self, text):
        """Sets the input text in the input area."""
        self.input_area.setText(text)

    def get_input(self):
        """Gets the current text from the input area."""
        return self.input_area.text()

    def set_output(self, text):
        """Sets the output text in the output area."""
        self.output_area.setText(text)

    def get_output(self):
        """Sets the output text in the output area."""
        return self.output_area.toPlainText()


app = QApplication(sys.argv)
main_window = MainWindow()

def start_main_window():
    global app, main_window

    main_window.show()
    sys.exit(app.exec_())