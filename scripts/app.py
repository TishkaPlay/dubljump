import pygame

from scripts.game import Game
from scripts.function import load_image

class App:

    def __init__(self):
        self.running = True
        self.maxFPS = 60

        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock()
    
        pygame.display.set_caption("DuDleJuMp")
        pygame.display.set_icon(load_image("assets", "icons", "icon.ico"))

        self.game = Game()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(self.maxFPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        ...
    
    def render(self):
        self.scene.fill((0,0,0))
        self.game.render_objekts(self.scene)
        pygame.display.update()