import pygame

#set screen up


#game class
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.display = pygame.display.set_mode((1280,720)) 

    def poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.display.fill("black")
        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.poll_events() 
            self.update()
            self.render()
        pygame.quit()

g= Game()
g.run
