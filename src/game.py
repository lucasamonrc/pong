import pygame
from pygame.locals import *
from objects import Paddle, Ball


class PongGame:
    def __init__(self, width, height):
        pygame.init()

        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Pong")

    def run(self):
        self.running = True
        self.clock = pygame.time.Clock()

        paddle = Paddle(30, 240)
        ball = Ball(320, 240)
        self.all_sprites = pygame.sprite.Group(paddle, ball)

        font = pygame.font.SysFont("Arial", 18, pygame.font.Font.bold)
        quit_text = font.render("QUIT", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect()
        quit_text_rect.center = (self.width // 2, self.height - 30)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN and quit_text_rect.collidepoint(event.pos):
                    pygame.quit()
                    self.running = False
                    break

            self.all_sprites.update()

            if pygame.sprite.collide_rect(ball, paddle):
                ball.speed_x = -ball.speed_x

            self.window.fill((0, 0, 0))
            self.window.blit(quit_text, quit_text_rect)
            self.all_sprites.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)
