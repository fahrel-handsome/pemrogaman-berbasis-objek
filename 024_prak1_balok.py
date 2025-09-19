class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    def luas_permukaan(self):
        return 2 * (self.panjang * self.lebar +
                    self.panjang * self.tinggi +
                    self.lebar * self.tinggi)

balok1 = Balok(10, 5, 4)
balok2 = Balok(7, 3, 6)

print("=== Balok 1 ===")
print(f"Panjang        : {balok1.panjang}")
print(f"Lebar          : {balok1.lebar}")
print(f"Tinggi         : {balok1.tinggi}")
print(f"Volume         : {balok1.volume()}")
print(f"Luas Permukaan : {balok1.luas_permukaan()}")
print()

print("=== Balok 2 ===")
print(f"Panjang        : {balok2.panjang}")
print(f"Lebar          : {balok2.lebar}")
print(f"Tinggi         : {balok2.tinggi}")
print(f"Volume         : {balok2.volume()}")
print(f"Luas Permukaan : {balok2.luas_permukaan()}")
