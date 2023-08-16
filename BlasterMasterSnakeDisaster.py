import pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.sprites = self.load_sprites()

    def poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.screen.fill("black")
        self.screen.blit(self.sprites["backround"],(0,0))
        self.screen.blit(self.sprites["spaceship"],(100,100))


        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.poll_events()
            self.update()
            self.render()
        pygame.quit()

    def load_sprites(self) -> dict:
        sprites = {}
        sprites["spaceship"]=pygame.image.load("gfx/ship.png").convert_alpha()
        sprites["backround"]=pygame.image.load("gfx/simple_game_bg.png").convert_alpha()
        sprites["spaceship"]=pygame.transform.scale(sprites["spaceship"],(40,40))
        return sprites


g = Game()
g.run()