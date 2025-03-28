import pygame
from entity import Entity
from player import Player

class Shot(Entity):
    def __init__(self, game, character):
        width = int(game.width * 0.015)
        height = int(game.height * 0.015)
        x = character.x + character.width // 2 - width // 2
        y = character.y
        speed = 10
        image_path = 'assets/shot1.png' if isinstance(character, Player) else 'assets/shot2.png'
        super().__init__(game, width, height, x, y, speed, image_path)

    def update(self):
        self.y -= self.speed if isinstance(self.game.player, Player) else self.speed
        if self.y < 0 or self.y > self.game.height:
            self.game.player_shots.remove(self) if isinstance(self.game.player, Player) else self.game.opponent_shots.remove(self)

    def __str__(self):
        return super().__str__() + ' (SHOT)'
    
