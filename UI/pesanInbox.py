from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

class FORM_UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("pesanInbox.ui", self)

app = QApplication(sys.argv)
window = FORM_UI()
window.setWindowTitle('Form Pesan Inbox')
window.show()
app.exec()