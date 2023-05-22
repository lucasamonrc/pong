import pygame
from pygame.locals import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 75])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[K_DOWN] and self.rect.bottom < 480:
            self.rect.move_ip(0, self.speed)
