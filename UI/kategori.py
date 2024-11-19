from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

class formKategori(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("kategori.ui", self)
