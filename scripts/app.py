import pygame
import os
from scripts.game import Game

class App:

    def __init__(self):
        self.running = True
        self.maxFPS = 60

        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock()
    
        pygame.display.set_caption("DuDleJuMp")
        image = pygame.image.load(os.path.join("assets", "icons", "icon.ico"))
        pygame.display.set_icon(image)

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