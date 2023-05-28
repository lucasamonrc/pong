import pygame
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, scoreboard):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = 5
        self.speed_y = 5
        self.scoreboard = scoreboard

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

        if self.rect.left <= 0 or self.rect.right >= 640:
            self.speed_x = -self.speed_x

        if self.rect.top <= 0 or self.rect.bottom >= 480:
            self.speed_y = -self.speed_y

        if self.rect.left <= 0:
            self.scoreboard.player_two_score += 1

        if self.rect.right >= 640:
            self.scoreboard.player_one_score += 1
