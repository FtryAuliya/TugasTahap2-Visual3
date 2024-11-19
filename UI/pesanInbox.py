from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class formPesan(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("pesanInbox.ui", self)
