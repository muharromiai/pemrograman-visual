# NAMA : Muharromi Ali Ilham
# NIM  : F1D02410082
# Kelas: Pemrograman Visual C
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFrame

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedWidth(400)
        self.setStyleSheet("background-color: #f5f5f5; font-family: sans-serif;")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        label_style = "color: #000;"
        input_style = """
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #28a745;
                border-radius: 4px;
                background-color: #eafbf0;
                font-size: 14px;
                color: #000;
            }
        """
        dropbox_style = """
            QComboBox {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: #ffffff;
                font-size: 14px;
                color: #333333;
            }

            QComboBox::drop-down {
                color: #000;
            }

            QComboBox QAbstractItemView {
                color: black;
            }
        """

        self.style_success = """
            QFrame {
                background-color: #d4edda;
                border-left: 5px solid #28a745;
                border-radius: 4px;
            }
            QLabel {
                color: #0f5132;
                background: transparent;
                border: none;
                padding: 2px 0px;
            }
        """
        
        self.style_error = """
            QFrame {
                background-color: #f8d7da;
                border-left: 5px solid #dc3545;
                border-radius: 4px;
            }
            QLabel {
                color: #842029;
                background: transparent;
                border: none;
                padding: 2px 0px;
            }
        """

        self.label_nama = QLabel("Nama Lengkap:")
        self.label_nama.setStyleSheet(label_style)
        self.edit_nama = QLineEdit()
        self.edit_nama.setStyleSheet(input_style)

        self.label_nim = QLabel("NIM:")
        self.label_nim.setStyleSheet(label_style)
        self.edit_nim = QLineEdit()
        self.edit_nim.setStyleSheet(input_style)
        self.edit_nim.setPlaceholderText("Masukkan NIM")

        self.label_kelas = QLabel("Kelas:")
        self.label_kelas.setStyleSheet(label_style)
        self.edit_kelas = QLineEdit()
        self.edit_kelas.setStyleSheet(input_style)
        self.edit_kelas.setPlaceholderText("TI-6C")

        self.label_jk = QLabel("Jenis Kelamin:")
        self.label_jk.setStyleSheet(label_style)
        self.combo_jk = QComboBox()
        self.combo_jk.setStyleSheet(dropbox_style)
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])

        self.btn_layout = QHBoxLayout()
        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_tampilkan.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #2980b9; }
        """)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border-radius: 4px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #7f8c8d; }
        """)

        self.btn_layout.addWidget(self.btn_tampilkan)
        self.btn_layout.addWidget(self.btn_reset)

        self.output_frame = QFrame()
        self.output_frame.setStyleSheet(self.style_success)
        self.output_layout = QVBoxLayout(self.output_frame)
        
        self.title_output = QLabel("DATA BIODATA")
        self.title_output.setStyleSheet("font-weight: bold; margin-bottom: 5px;")
        
        self.res_nama = QLabel("")
        self.res_nim = QLabel("")
        self.res_kelas = QLabel("")
        self.res_jk = QLabel("")

        self.output_layout.addWidget(self.title_output)
        self.output_layout.addWidget(self.res_nama)
        self.output_layout.addWidget(self.res_nim)
        self.output_layout.addWidget(self.res_kelas)
        self.output_layout.addWidget(self.res_jk)

        self.main_layout.addWidget(self.label_nama)
        self.main_layout.addWidget(self.edit_nama)
        self.main_layout.addWidget(self.label_nim)
        self.main_layout.addWidget(self.edit_nim)
        self.main_layout.addWidget(self.label_kelas)
        self.main_layout.addWidget(self.edit_kelas)
        self.main_layout.addWidget(self.label_jk)
        self.main_layout.addWidget(self.combo_jk)
        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addWidget(self.output_frame)

        self.setLayout(self.main_layout)

        self.btn_tampilkan.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_data)

    def tampilkan_data(self):
        nama = self.edit_nama.text().strip()
        nim = self.edit_nim.text().strip()
        kelas = self.edit_kelas.text().strip()
        jk = self.combo_jk.currentText()

        if not nama or not nim or not kelas:
            self.output_frame.setStyleSheet(self.style_error)
            self.res_nama.setText("Lengkapi semua data!")
            self.res_nim.setText("")
            self.res_kelas.setText("")
            self.res_jk.setText("")
        else:
            self.output_frame.setStyleSheet(self.style_success)
            self.res_nama.setText(f"Nama: {nama}")
            self.res_nim.setText(f"NIM: {nim}")
            self.res_kelas.setText(f"Kelas: {kelas}")
            self.res_jk.setText(f"Jenis Kelamin: {jk}")

    def reset_data(self):
        self.edit_nama.clear()
        self.edit_nim.clear()
        self.edit_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        
        self.output_frame.setStyleSheet(self.style_success)
        self.res_nama.setText("")
        self.res_nim.setText("")
        self.res_kelas.setText("")
        self.res_jk.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())