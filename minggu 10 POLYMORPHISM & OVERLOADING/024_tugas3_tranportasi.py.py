class Transportasi:
    def bergerak(self):
        print("Transportasi bergerak...")

class Mobil(Transportasi):
    def bergerak(self):
        print("Mobil bergerak di jalan raya.")

class Kapal(Transportasi):
    def bergerak(self):
        print("Kapal berlayar di laut.")

class Pesawat(Transportasi):
    def bergerak(self):
        print("Pesawat terbang di udara.")

if __name__ == "__main__":
    armada = [Mobil(), Kapal(), Pesawat()]
    for t in armada:
        t.bergerak()