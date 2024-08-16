import pygame
pygame.init()

screen = pygame.display.set_mode((474, 266))
pygame.display.set_caption("FPS Game")
# Memuat gambar
image = pygame.image.load('wallpaper.jpg')

# Loop utama permainan
x=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar
    screen.blit(image, (0,0))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()