import random
import pygame
from visuals import GameState

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("spaceship.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 568
        self.rect.y = 460
        self.speedX = 2
        self.speedY = 2
        self.health = 3
        self.points = 0

    def move(self, X, Y, game_state):
        if game_state == GameState.PAUSE:
            pass
        else:
            self.rect.x += X * self.speedX
            self.rect.y += Y * self.speedY

    def update(self, asteroid):
        hit_list = pygame.sprite.spritecollide(self, asteroid, True, collided=pygame.sprite.collide_rect_ratio(0.75))
        for enemy in hit_list:
            self.health -= 1
            print(self.health)

    def fire(self, missiles):
        missile = Missile(self.rect.x, self.rect.y)
        missiles.add(missile)
        return missiles

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("asteroid.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1100)
        self.rect.y = random.randint(-200, -100)
        self.speedY = 1

    def update(self, player, missile, game_state):
        if game_state == GameState.PAUSE:
            pass
        else:
            self.rect.y += self.speedY
            if self.rect.y >= 700:
                self.rect.x = random.randint(0, 1100)
                self.rect.y = random.randint(-200, -100)
            pygame.sprite.spritecollide(self, player, False)
            pygame.sprite.spritecollide(self, missile, True)

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("torpedo.png")
        img = pygame.transform.rotate(img, -90)
        img = pygame.transform.scale(img, (32, 32))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedY = -2

    def update(self, asteroid, player, game_state):
        if game_state == GameState.PAUSE:
            pass
        else:
            self.rect.y += self.speedY
            if self.rect.y <= -10:
                self.kill()
            if pygame.sprite.spritecollide(self, asteroid, True, collided=pygame.sprite.collide_rect_ratio(1.25)):
                player.points += 100
                self.kill()

if __name__ == "__main__":
    pass