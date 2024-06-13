from scripts.sprite import Sprite

class Player(Sprite):
    def __init__(self, center, image, speed, jump_power, gravity):
        super().__init__(image, center)
        self.speed = speed
        self.jump_power = jump_power
        self.gravity = gravity  
        self.walking_right = False
        self.walking_left = False
        self.velocity_y = 0
        self.on_platform = False

    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect.y += self.velocity_y

        if self.walking_left != self.walking_right:
            if self.walking_left:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed