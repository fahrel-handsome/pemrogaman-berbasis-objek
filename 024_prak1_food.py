class MenuItem:
    def __init__(self, nama, harga, keterangan):
        self.nama = nama
        self.harga = harga
        self.keterangan = keterangan

    def info(self):
        return f"{self.nama}: Rp{self.harga} ({self.keterangan})"

    def total_harga(self, jumlah):
        total = self.harga * jumlah
        # Diskon 10% kalau beli 3 atau lebih
        if jumlah >= 3:
            total *= 0.9
        return total

menu = [
    MenuItem("Nasi Goreng", 15000, "Porsi lengkap"),
    MenuItem("Ayam Goreng", 12000, "Dada/Paha + sambal"),
    MenuItem("Tahu Tempe", 5000, "Isi 2 potong"),
    MenuItem("Sayur Sop", 8000, "Dengan sayuran segar"),
    MenuItem("Rahang Tuna", 40000, "Porsi lengkap"),
    MenuItem("Lele Goreng", 12000, "Porsi lengkap")
]

print("=== MENU WARTEG ===")
for i, item in enumerate(menu, 1):
    print(f"{i}. {item.info()}")

menu_number = int(input("\nMasukkan nomor menu yang ingin dipesan: "))
pilihan = menu[menu_number - 1]

jumlah = int(input("Mau pesan berapa porsi? (Diskon 10% untuk 3 atau lebih): "))

total = pilihan.total_harga(jumlah)

print("\n=== STRUK PESANAN ===")
print(f"Menu   : {pilihan.nama}")
print(f"Jumlah : {jumlah}")
print(f"Total  : Rp{int(total)}")
print("====================")
