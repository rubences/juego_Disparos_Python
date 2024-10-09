import pygame 
from entity import Entity

class Character(Entity):
    def __init__(self, game, width, height, x, y, speed, image_path, dead_image_path):
        super().__init__(game, width, height, x, y, speed, image_path)
        self.dead = False
        self.dead_image = pygame.image.load(dead_image_path)

    def collide(self, other):
        return self.rect.colliderect(other.rect)

    def collide_with_opponent(self):
        self.dead = True

    def collide_with_player(self):
        self.dead = True
        pygame.time.set_timer(pygame.USEREVENT, 2000)
