class Novel:
    def __init__(self, judul, pengarang, tahun_terbit, deskripsi, harga_beli):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__deskripsi = deskripsi
        self.__harga_beli = harga_beli

    # Getter untuk mengambil data
    def get_judul(self):
        return self.__judul

    def get_harga_beli(self):
        return self.__harga_beli

    # Method untuk menghitung harga jual
    def hitung_harga_jual(self):
        return self.__harga_beli - (0.2 * self.__harga_beli)

    # Method untuk menampilkan info novel
    def get_info(self):
        print(f"Judul        : {self.__judul}")
        print(f"Pengarang    : {self.__pengarang}")
        print(f"Tahun Terbit : {self.__tahun_terbit}")
        print(f"Deskripsi    : {self.__deskripsi}")
        print(f"Harga Beli   : Rp{self.__harga_beli:,.0f}")
        print(f"Harga Jual   : Rp{self.hitung_harga_jual():,.0f}")
        print("-" * 40)

# Membuat 3 objek novel
novel1 = Novel("Harry Poter", "Joanne Rowling", 1997, "kisah penyihir muda bernama Harry Potter, yang mengetahui bahwa dirinya adalah seorang penyihir di ulang tahunnya yang ke-11, dan kemudian bersekolah di Sekolah Sihir Hogwarts bersama sahabatnya, Ron Weasley dan Hermione Granger.", 7500000)
novel2 = Novel("Laskar Pelangi", "Andrea Hirata", 2005, "semangat persahabatan dan perjuangan anak-anak miskin di Pulau Belitung untuk mendapatkan pendidikan di tengah keterbatasan dan kemiskinan.", 5000000)
novel3 = Novel("3726 Mpdl", "Nurwina Sari", 2024, "isah cinta antara Rangga Raja dan Andini Hangura, yang berlatar di lingkungan mahasiswa dan pendakian Gunung Rinjani.", 1200000)

# Menampilkan info tiap buku
novel1.get_info()
novel2.get_info()
novel3.get_info()

# Hitung total beli & jual
total_beli = novel1.get_harga_beli() + novel2.get_harga_beli() + novel3.get_harga_beli()
total_jual = novel1.hitung_harga_jual() + novel2.hitung_harga_jual() + novel3.hitung_harga_jual()

print(f"Total Harga Beli Semua Buku : Rp{total_beli:,.0f}")
print(f"Total Harga Jual Semua Buku : Rp{total_jual:,.0f}")
