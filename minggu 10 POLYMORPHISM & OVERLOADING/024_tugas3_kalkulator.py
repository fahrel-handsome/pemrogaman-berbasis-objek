class Kalkulator:
    def hitung(self, a=None, b=None, c=None):
        
        if a is not None and b is not None and c is not None:
            print(f"Menjumlahkan tiga angka: {a} + {b} + {c}")
            return a + b + c
        
        elif a is not None and b is not None:
            print(f"Menjumlahkan dua angka: {a} + {b}")
            return a + b
        
        else:
            print("Parameter tidak cukup! (minimal 2 angka)")
            return None


def minta_angka(n):
    """Minta n buah angka dari pengguna dan kembalikan sebagai list float."""
    hasil = []
    for i in range(1, n+1):
        while True:
            try:
                val = float(input(f"Masukkan angka ke-{i}: "))
                hasil.append(val)
                break
            except ValueError:
                print("Input tidak valid. Coba lagi.")
    return hasil


def main():
    kalk = Kalkulator()
    while True:
        print("\n=== Menu Kalkulator (Overloading) ===")
        print("1. Jumlahkan 2 angka")
        print("2. Jumlahkan 3 angka")
        print("3. Contoh error (coba hanya 1 angka)")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            a, b = minta_angka(2)
            hasil = kalk.hitung(a, b)
            print("Hasil:", hasil)
        elif pilihan == "2":
            a, b, c = minta_angka(3)
            hasil = kalk.hitung(a, b, c)
            print("Hasil:", hasil)
        elif pilihan == "3":
            a, = minta_angka(1)
            hasil = kalk.hitung(a)   # kurang dari 2 parameter -> pesan error
            print("Hasil:", hasil)
        elif pilihan == "0":
            print("bye bye...")
            break
        else:
            print("Menu tidak dikenal, silakan pilih lagi.")


if __name__ == "__main__":
    main()