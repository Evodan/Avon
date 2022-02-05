import sys

import keyboard

import Nessa.ActiveMind as ActiveMind_A
from Nessa import Core
import PyQt6.QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QTextEdit


class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nessa")  # TODO Accept Avon Loaded into Environment
        self.resize(300, 400)  # width, height

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()

        self.output = QTextEdit()

        layout.addWidget(self.inputField),
        layout.addWidget(self.output)

        self.inputField.returnPressed.connect(self.Talk)

    def Talk(self):
        inputText = self.inputField.text()
        ActiveMind_A.AddToAMem(ActiveMind_A, 'You: {0}'.format(inputText))
        ActiveMind_A.Comprhend(ActiveMind_A)
        self.output.setText(ActiveMind_A.AutoMemory())


TextApp = QApplication(sys.argv)
TextApp.setStyleSheet('''
    QWidget {
        font-size: 15px;
    }
''')

window = ChatApp()
window.show()

TextApp.exec()

TextApp.quitOnLastWindowClosed()
