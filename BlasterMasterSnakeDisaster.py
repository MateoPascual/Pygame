import pygame, random, time

class Collectible:
    def __init__(self, x: float, y: float, sprite: pygame.Surface) -> None:
        self.x = x
        self.y = y
        self.sprite = sprite

    def update(self) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.sprite, (self.x, self.y))

    def randomize_position(self) -> None:
        self.x = random.randint(50, 1250)
        self.y = random.randint(50, 670)

class Player:
    def __init__(self, x: float, y: float, sprite: pygame.Surface) -> None:
        self.x = x
        self.y = y
        self.sprite = sprite
        self.velocity = 200
        self.angle = 0
        self.direction = "up"
        self.moving = False

    def update(self, dt) -> None:
        if self.moving:
            self.move(dt)

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.sprite, (self.x, self.y))

    def set_angle(self, new_angle: int) -> None:
        rotation = new_angle - self.angle
        self.sprite = pygame.transform.rotate(self.sprite, rotation)
        self.angle = new_angle

    def move(self, dt) -> None:
        if self.direction == "up":
            self.y -= self.velocity * dt
        elif self.direction == "down":
            self.y += self.velocity * dt
        elif self.direction == "left":
            self.x -= self.velocity * dt
        elif self.direction == "right":
            self.x += self.velocity * dt

        self.x = min((1280, self.x))
        self.x = max((0, self.x))

        self.y = min((720, self.y))
        self.y = max((0, self.y))


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.sprites = self.load_sprites()

        self.player = Player(200, 200, self.sprites["spaceship"])
        self.collectible = Collectible(500, 500, self.sprites["collectible"])
        self.collectible.randomize_position()

        self.keybinds = {pygame.K_w: (0, "up"),
                         pygame.K_d: (270, "right"),
                         pygame.K_s: (180, "down"),
                         pygame.K_a: (90, "left")}

    def poll_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN and event.key in self.keybinds:
                self.player.set_angle(self.keybinds[event.key][0])
                self.player.direction = self.keybinds[event.key][1]
                self.player.moving = True

            if event.type == pygame.KEYUP and event.key in self.keybinds:
                if self.keybinds[event.key][1] == self.player.direction:
                    self.player.moving = False

    def update(self) -> None:
        # Compute delta time
        now = time.time()
        dt = now - self.previous_time
        self.previous_time = now


        self.player.update(dt)
        self.collectible.update()

    def render(self) -> None:
        self.screen.fill("black")
        
        self.screen.blit(self.sprites["background"], (0, 0))
        self.player.render(self.screen)
        self.collectible.render(self.screen)

        pygame.display.update()

    def run(self) -> None:
        self.previous_time = time.time()
        while self.running:
            self.poll_events()
            self.update()
            self.render()
        pygame.quit()

    def load_sprites(self) -> dict:
        sprites = {}

        sprites["spaceship"] = pygame.image.load("gfx/ship.png").convert_alpha()
        sprites["background"] = pygame.image.load("gfx/simple_game_bg.png").convert_alpha()
        sprites["collectible"] = pygame.image.load("gfx/collectible.png").convert_alpha()

        # Downscale
        sprites["spaceship"] = pygame.transform.scale(sprites["spaceship"], (48, 48))

        return sprites
print('hello')
g = Game()
g.run()