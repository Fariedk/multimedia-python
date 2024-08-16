import pygame
pygame.init()

screen = pygame.display.set_mode((474, 266))
pygame.display.set_caption("FPS Game")
# Memuat gambar
image = pygame.image.load('wallpaper.jpg')
sound = pygame.mixer.Sound ('yoasobi.mp3')

#loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 2
    if x > 500:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))
    
    sound.play()

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()