# Superclass
class Hewan:
    def bersuara(self):
        print("Hewan bersuara...")

# Subclass
class Kucing(Hewan):
    # override
    def bersuara(self):
        print("Kucing: Meong...")

class Anjing(Hewan):
    # override
    def bersuara(self):
        print("Anjing: Guk guk...")

class Burung(Hewan):
    # override
    def bersuara(self):
        print("Burung: Cuit cuit...")

# Polimorfisme
daftar_hewan = [Kucing(), Anjing(), Burung()]
for h in daftar_hewan:
    h.bersuara()