import pygame

#set screen up


#game class
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.display = pygame.display.set_mode((1280,720)) 
        self.sprites = self.load_sprite()

    def poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.display.fill("black")
        pygame.display.update()
        #render 

    def run(self) -> None:
        while self.running:
            self.poll_events() 
            self.update()
            self.render()
        pygame.quit()

    def load_sprite(self) -> dict:
        sprites = {}

        sprites["player"] = pygame.image.load("pygame/ship.png").convert_alpha()

        return sprites
    



g= Game()
g.run
