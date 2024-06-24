import pygame
from scripts.function import load_image
from random import randint
from scripts.constants import display_size, createplatformevent
from scripts.platform import Platform, MovingPlatform


class platform_generate:
    def __init__(self, step):
        self.step = step

    def create_start_configuration(self): 
        platform = Platform(
            load_image("assets", "images", "platform.png"),
            [display_size[0] / 2, display_size[1] - 50],
        )

        event = pygame.Event(createplatformevent, {"platform": platform})
        pygame.event.post(event)

        for y in range(display_size[1], 0, -self.step):
            self.create_plaform(y)

    def create_plaform(self, center_y):

        r = randint(0,100)

        if r > 77:
            image = load_image("assets", "images", "moving-platform.png")
        else:
            image = load_image("assets", "images", "platform.png")

            
        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)

        if r > 77:
            speed = randint(100,1000) / 100
            platform = MovingPlatform(image, (center_x, center_y), speed)
        else:
            platform = Platform(image, [center_x, center_y])

        event = pygame.Event(createplatformevent, {"platform": platform})
        pygame.event.post(event)

    def update(self, offset_y, platforms):
        if platforms and platforms[-1].rect.centery - offset_y >= self.step:
            self.create_plaform(offset_y)
            platforms.remove(platforms[0])
        
