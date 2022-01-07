import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout


class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nessa")  # TODO Accept Avon Loaded into Environment
        self.resize(300, 200)  # width, height


TextApp = QApplication([])

TextApp.exec()

TextApp.quitOnLastWindowClosed()