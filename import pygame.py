import pygame
pygame.init()


todisplay = pygame.display.set_mode((1280, 720))

run=True
while run:
    todisplay.fill("black")

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()