import tkinter as tk

class Animal:
    def make_sound(self):
        return "Suara hewan umum"
    
# Kelas turunan cat
class Cat(Animal):
    def make_sound(self):
        return "mweeoonnggggg"

# Kelas turunan Bird
class Bird(Animal):
    def make_sound(self):
        return "Tweet tweet"

# Kelas turunan Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"

# Kelas turunan Snake
class Snake(Animal):
    def make_sound(self):
        return "ssssstttttt"
    
# Kelas turunan Tokek
class Gecko(Animal):
    def make_sound(self):
        return "Tok tok tok tok otok tekeekkkkk"

root = tk.Tk()
root.geometry("500x350")
root.title("Polimorfisme di Tkinter")

label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan.", font=("Arial", 14))
label_result.pack(pady=20)

# Fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih
def show_sound(animal):
    label_result.config(text=animal.make_sound())

# Tombol untuk memilih cat
button_animal = tk.Button(root, text="Kucing", font=("Arial", 12), command=lambda: show_sound(Cat()))
button_animal.pack(pady=10)

# Tombol untuk memilih Burung
button_bird = tk.Button(root, text="Burung", font=("Arial", 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Anjing", font=("Arial", 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

# Tombol untuk memilih Ular
button_dog = tk.Button(root, text="Ular", font=("Arial", 12), command=lambda: show_sound(Snake()))
button_dog.pack(pady=10)

# Tombol untuk memilih Anjing
button_dog = tk.Button(root, text="Tokek", font=("Arial", 12), command=lambda: show_sound(Gecko()))
button_dog.pack(pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
