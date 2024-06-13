import pygame
from scripts.function import load_image
from scripts.sprite import Sprite
from scripts.player import Player

class Game:
    def __init__(self): 
        self.background = load_image("assets", "images", "background.png")
        self.platforms = [
            Sprite(load_image("assets", "images", "platform.png"), [240,700])
        ]

        self.player = Player(
            load_image("assets", "images", "player.png"),
            (240, 600),
            5,
            15,
            0.75,
        )

    def process_key_down_event(self, key):
        if key == pygame.K_a:
            self.player.walking_left = True
        if key == pygame.K_d:
            self.player.walking_right = True
    def process_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.walking_left = False
        if key == pygame.K_d:
            self.player.walking_right = False

    def render_objekts(self, scene):
        scene.blit(self.background, (0,0))
        for platform in self.platforms:
            platform.render(scene)
        self.player.render(scene)
    
    def update_objekts(self):
        self.player.update()
        
