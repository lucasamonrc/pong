import pygame
from pygame.locals import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, player_one=True):
        super().__init__()
        self.image = pygame.Surface([10, 75])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

        if player_one:
            self.key_up = K_w
            self.key_down = K_s
        else:
            self.key_up = K_UP
            self.key_down = K_DOWN

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[self.key_up] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[self.key_down] and self.rect.bottom < 480:
            self.rect.move_ip(0, self.speed)
