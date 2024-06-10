class Sprite:
    def __init__(self, image, center):
        self.image = image 
        self.rect = image.get_frect()
        self.rect.center = center
        
    def render(self, scene):
        scene.blit(self.image, self.rect)

    def collide(self, other_rect):
        return self.rect.colliderect(other_rect)