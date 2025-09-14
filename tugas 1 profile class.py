class DataDiri:
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    def tampilan_data(self):
        print("Nama      :", self.nama)
        print("Kelas     :", self.kelas)
        print("NIM       :", self.nim)
        print("Jurusan   :", self.jurusan)
        print("Fakultas  :", self.fakultas)
        print("Kampus    :", self.kampus)


# Membuat object
data_saya = DataDiri(
    "Fahrel Ilham", "2024A", "24091397024",
    "Manajemen Informatika", "Vokasi", "Universitas Negeri Surabaya"
)

# Menampilkan data
data_saya.tampilan_data()
