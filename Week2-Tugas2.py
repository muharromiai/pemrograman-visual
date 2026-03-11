import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Konversi Suhu")
        self.setFixedWidth(400)
        self.setStyleSheet("background-color: #f8f9fa; font-family: sans-serif;")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        self.header_label = QLabel("KONVERSI SUHU")
        self.header_label.setStyleSheet("""
            background-color: #3498db;
            color: white;
            padding: 15px;
            font-weight: bold;
            font-size: 16px;
            border-radius: 4px;
        """)
        self.header_label.setAlignment(self.header_label.alignment().AlignCenter)

        self.label_suhu = QLabel("Masukkan Suhu (Celsius):")
        self.label_suhu.setStyleSheet("color: #555; font-size: 13px;")
        
        self.edit_suhu = QLineEdit()
        self.edit_suhu.setPlaceholderText("Contoh: 100")
        self.edit_suhu.setStyleSheet("""
            padding: 10px;
            border: 1px solid #28a745;
            border-radius: 4px;
            background-color: #eafbf0;
            font-size: 14px;
            color: black;
        """)

        self.btn_layout = QHBoxLayout()
        
        btn_style = """
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 4px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #2980b9; }
        """

        self.btn_f = QPushButton("Fahrenheit")
        self.btn_f.setStyleSheet(btn_style)
        
        self.btn_k = QPushButton("Kelvin")
        self.btn_k.setStyleSheet(btn_style)
        
        self.btn_r = QPushButton("Reamur")
        self.btn_r.setStyleSheet(btn_style)

        self.btn_layout.addWidget(self.btn_f)
        self.btn_layout.addWidget(self.btn_k)
        self.btn_layout.addWidget(self.btn_r)

        self.style_success = """
            QFrame {
                background-color: #cce5ff;
                border-left: 5px solid #004085;
                border-radius: 4px;
            }
            QLabel {
                color: #004085;
                background: transparent;
                border: none;
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
            }
        """

        self.output_frame = QFrame()
        self.output_frame.setStyleSheet(self.style_success)
        self.output_layout = QVBoxLayout(self.output_frame)
        self.output_layout.setSpacing(10)
        
        self.title_output = QLabel("Hasil Konversi:")
        self.title_output.setStyleSheet("font-weight: bold; font-size: 13px;")
        
        self.res_hasil = QLabel("")
        self.res_hasil.setStyleSheet("font-size: 14px;")

        self.output_layout.addWidget(self.title_output)
        self.output_layout.addWidget(self.res_hasil)

        self.main_layout.addWidget(self.header_label)
        self.main_layout.addWidget(self.label_suhu)
        self.main_layout.addWidget(self.edit_suhu)
        self.main_layout.addLayout(self.btn_layout)
        self.main_layout.addWidget(self.output_frame)

        self.setLayout(self.main_layout)

        self.btn_f.clicked.connect(self.hitung_ke_fahrenheit)
        self.btn_k.clicked.connect(self.hitung_ke_kelvin)
        self.btn_r.clicked.connect(self.hitung_ke_reamur)

    def hitung_ke_fahrenheit(self):
        self.hitung_konversi("Fahrenheit")

    def hitung_ke_kelvin(self):
        self.hitung_konversi("Kelvin")

    def hitung_ke_reamur(self):
        self.hitung_konversi("Reamur")

    def hitung_konversi(self, satuan):
        teks_input = self.edit_suhu.text().strip()

    def hitung_konversi(self, satuan):
        teks_input = self.edit_suhu.text().strip()

        if not teks_input:
            self.tampilkan_error("Masukkan suhu dalam celsius!")
            return

        try:
            celsius = float(teks_input)
        except ValueError:
            self.tampilkan_error("Input harus berupa angka!")
            return

        self.output_frame.setStyleSheet(self.style_success)
        
        if satuan == "Fahrenheit":
            hasil = (celsius * 9/5) + 32
        elif satuan == "Kelvin":
            hasil = celsius + 273.15
        elif satuan == "Reamur":
            hasil = celsius * 4/5

        teks_hasil = f"Celsius = {hasil:.2f} {satuan}"
        self.res_hasil.setText(teks_hasil)

    def tampilkan_error(self, pesan):
        self.output_frame.setStyleSheet(self.style_error)
        self.res_hasil.setText(pesan)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())