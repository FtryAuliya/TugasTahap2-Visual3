from PyQt6.QtWidgets import QMainWindow,QPushButton
from PyQt6.uic import loadUi
from iklan import formIklan
from kategori import formKategori
from kota import formKota
from member import formMember
from pembayaran import formPembayaran
from pesanInbox import formPesan

class formUtama(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('formUtama.ui',self)
        self.button_tampil_iklan = self.findChild(QPushButton, "button_tampil_iklan")
        self.button_tampil_kategori = self.findChild(QPushButton, "button_tampil_kategori")
        self.button_tampil_kota = self.findChild(QPushButton, "button_tampil_kota")
        self.button_tampil_member = self.findChild(QPushButton, "button_tampil_member")
        self.button_tampil_pembayaran = self.findChild(QPushButton, "button_tampil_pembayaran")
        self.button_tampil_pesan = self.findChild(QPushButton, "button_tampil_pesan")

        self.button_tampil_iklan.clicked.connect(self.tampil_iklan)
        self.button_tampil_kategori.clicked.connect(self.tampil_kategori)
        self.button_tampil_kota.clicked.connect(self.tampil_kota)
        self.button_tampil_member.clicked.connect(self.tampil_member)
        self.button_tampil_pembayaran.clicked.connect(self.tampil_pembayaran)
        self.button_tampil_pesan.clicked.connect(self.tampil_pesan)

    def tampil_iklan(self):
        self.iklan = formIklan()
        self.iklan.show()
        # self.close()

    def tampil_kategori(self):
        self.kategori = formKategori()
        self.kategori.show()
        #self.close()

    def tampil_kota(self):
        self.kota = formKota()
        self.kota.show()
        # self.close()

    def tampil_member(self):
        self.member = formMember()
        self.member.show()
        # self.close()

    def tampil_pembayaran(self):
        self.pembayaran = formPembayaran()
        self.pembayaran.show()
        # self.close()

    def tampil_pesan(self):
        self.pesanInbox = formPesan()
        self.pesanInbox.show()
        # self.close()
