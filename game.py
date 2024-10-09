import pygame
from player import Player
from opponent import Opponent
from boss import Boss
from shot import Shot

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self)
        self.opponent = Opponent(self)
        self.player_shots = []
        self.opponent_shots = []
        self.score = 0
        self.ended = False
        self.font = pygame.font.Font(None, 36)
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.USEREVENT and self.player.dead:
                    self.player.image = pygame.image.load('assets/bueno.png')
                    self.player.dead = False
            
            keys = pygame.key.get_pressed()
            self.update(keys)
            self.render()
            self.clock.tick(60)
        
        pygame.quit()

    def update(self, keys):
        if not self.ended:
            self.player.update(keys)
            self.opponent.update()
            for shot in self.player_shots:
                shot.update()
            for shot in self.opponent_shots:
                shot.update()
            self.check_collisions()

    def render(self):
        self.screen.fill((0, 0, 0))
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lives_text = self.font.render(f'Lives: {self.player.lives}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.player.render()
        self.opponent.render()
        for shot in self.player_shots:
            shot.render()
        for shot in self.opponent_shots:
            shot.render()
        pygame.display.flip()

    def shoot(self, character):
        if isinstance(character, Player):
            self.player_shots.append(Shot(self, character))
        else:
            self.opponent_shots.append(Shot(self, character))

    def check_collisions(self):
        if self.player.collide(self.opponent):
            self.player.collide_with_opponent()
        if self.opponent.collide(self.player):
            self.opponent.collide_with_player()

    def remove_opponent(self):
        if isinstance(self.opponent, Boss):
            self.end_game(True)
        else:
            self.opponent = Boss(self)

    def end_game(self, won=False):
        self.ended = True
        if won:
            game_over_image = pygame.image.load('assets/you_win.png')
        else:
            game_over_image = pygame.image.load('assets/game_over.png')
        self.screen.blit(game_over_image, (self.width // 4, self.height // 4))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.running = False
