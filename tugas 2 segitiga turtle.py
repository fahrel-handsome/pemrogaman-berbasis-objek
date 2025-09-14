import turtle

class MyTurtle:
    def __init__(self, color, shape):
        # Membuat objek turtle
        self.t = turtle.Turtle()  # Object dari class Turtle
        self.t.color(color)  # Mengatur warna turtle
        self.t.shape(shape)  # Mengatur bentuk turtle

    def maju(self, jarak):
        # Method untuk menggerakkan turtle maju
        self.t.forward(jarak)

    def putar_kanan(self, sudut):
        # Method untuk memutar turtle ke kanan
        self.t.right(sudut)
    def buat_segitiga(self, ukuran):
        # Method untuk menggambar persegi
        for _ in range(3):
            self.maju(ukuran)
            self.putar_kanan(- 120)  # Sudut 60 derajat untuk persegi

    def selesai(self):
        # Method untuk menyelesaikan gambar
        turtle.done()

# Membuat objek turtle dengan warna dan bentuk
turtle1 = MyTurtle("purple", "turtle")

# Menggambar segitiga dengan ukuran sisi 150
turtle1.buat_segitiga(150)

# Menyelesaikan gambar
turtle1.selesai()