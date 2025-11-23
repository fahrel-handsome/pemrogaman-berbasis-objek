import pygame
import sys

# 2. Inisialisasi pygame dan suara
pygame.init()
pygame.mixer.init() # suara

# 3. Menambahkan suara dan melakukan looping
pygame.mixer.music.load("mars.mp3")
pygame.mixer.music.play(-1) # -1 artinya looping terus

# 4. Tambahkan Gambar
image = pygame.image.load("logo_unesa.png")

# 5. Tambahkan ukuran window dan title
# Ukuran Jendela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menampilkan Gambar + BackSound")

# 6. Mengubah ukuran gambar (opsional)
# (opsional) Ubah ukuran gambar
image = pygame.transform.scale(image, (300, 150))

# 7. Setting posisi gambar ditengah
# Posisi gambar di tengah
x = (width // 2) - (image.get_width() // 2)
y = (height // 2) - (image.get_height() // 2)

# 8. Main loop
# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255)) # background putih
    screen.blit(image, (x, y)) # tampilkan gambar
    pygame.display.update()
    
    