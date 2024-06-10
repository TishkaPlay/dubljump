import pygame
from scripts.function import load_image
from scripts.sprite import Sprite

class Game:
    def __init__(self):
        self.background = load_image("assets", "images", "background.png")
        self.platforms = [
            Sprite(load_image("assets", "images", "platform.png"), [240,700])
        ]


    def render_objekts(self, scene):
        scene.blit(self.background, (0,0))
        for platform in self.platforms:
            platform.render(scene)
        
