import pygame
pygame.init()
#set screen up
display = pygame.display.set_mode((1280,720)) 
#while run condition is true keep screen open
run = True
while run:
    display.fill("black")

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()