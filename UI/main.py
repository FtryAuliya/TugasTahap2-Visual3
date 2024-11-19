import sys
from PyQt6.QtWidgets import QApplication
from formUtama import formUtama

if __name__ == "__main__":
    aplikasi =QApplication(sys.argv)
    tampilForm = formUtama()
    tampilForm.show()
    sys.exit(aplikasi.exec())