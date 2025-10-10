# Superclass
class Enemy:
    def __init__(self, name, hp, attack_point):
        self.name = name
        self.hp = hp
        self.attack_point = attack_point

    def attack(self):
        print(f"{self.name} menyerang dengan kekuatan {self.attack_point}!")

# Subclass 1
class Zombie(Enemy):
    def walk(self):
        print(f"{self.name} berjalan perlahan seperti zombie...")

# Subclass 2
class Pocong(Enemy):
    def jump(self):
        print(f"{self.name} melompat seperti pocong!")

# Subclass 3
class Burung(Enemy):
    def fly(self):
        print(f"{self.name} terbang tinggi di langit!")

    def walk(self):
        print(f"{self.name} berjalan dengan kedua sayapnya.")

    def jump(self):
        print(f"{self.name} melompat kecil sebelum terbang.")

# Testing
if __name__ == "__main__":
    zombie = Zombie("Zombie Hijau", 100, 20)
    pocong = Pocong("Pocong Seram", 120, 25)
    burung = Burung("Elang Hitam", 80, 15)

    # Zombie
    zombie.attack()
    zombie.walk()

    print()  # pemisah output

    # Pocong
    pocong.attack()
    pocong.jump()

    print()

    # Burung
    burung.attack()
    burung.fly()
    burung.walk()
    burung.jump()
