from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLineEdit
import sys


# Kelas utama untuk mengatur GUI dan QFileDialog
class FORM_UI(QMainWindow):
    def __init__(self):
        super(FORM_UI, self).__init__()
        uic.loadUi("iklan.ui", self)  # Memuat file .ui yang dibuat dengan Qt Designer

        # Temukan tombol dan line edit dari file .ui
        self.button_browse_image1 = self.findChild(QPushButton, "button_browse_image1")
        self.button_browse_image2 = self.findChild(QPushButton, "button_browse_image2")
        self.button_browse_image3 = self.findChild(QPushButton, "button_browse_image3")

        self.line_edit_file_path = self.findChild(QLineEdit, "line_edit_file_path1")
        self.line_edit_file_path = self.findChild(QLineEdit, "line_edit_file_path2")
        self.line_edit_file_path = self.findChild(QLineEdit, "line_edit_file_path3")

        # Hubungkan tombol ke fungsi browse_file
        self.button_browse_image1.clicked.connect(self.image_file1)
        self.button_browse_image2.clicked.connect(self.image_file2)
        self.button_browse_image3.clicked.connect(self.image_file3)

    def image_file1(self):
        # Membuka dialog pemilihan file
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Image Files (*.png *.jpg *.bmp)")

        # Menampilkan nama file yang dipilih di QLineEdit
        if file_name:
            self.line_edit_file_path1.setText(file_name)

    def image_file2(self):
        # Membuka dialog pemilihan file
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Image Files (*.png *.jpg *.bmp)")

        # Menampilkan nama file yang dipilih di QLineEdit
        if file_name:
            self.line_edit_file_path2.setText(file_name)

    def image_file3(self):
        # Membuka dialog pemilihan file
        file_name, _ = QFileDialog.getOpenFileName(self, "Pilih Gambar", "", "Image Files (*.png *.jpg *.bmp)")

        # Menampilkan nama file yang dipilih di QLineEdit
        if file_name:
            self.line_edit_file_path3.setText(file_name)


app = QApplication(sys.argv)
window = FORM_UI()
window.setWindowTitle('Form Iklan')
window.show()
sys.exit(app.exec())
