import pygame

class Entity:
    def __init__(self, game, width, height, x, y, speed, image_path):
        self.game = game
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def render(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def __str__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return self.y < other.y
    
    def __le__(self, other):
        return self.y <= other.y
    
    def __gt__(self, other):
        return self.y > other.y
    
