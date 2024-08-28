from PyQt5.QtWidgets import QMessageBox, QApplication
import sys

def show_error(message):
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Error")
    msg.exec_()
