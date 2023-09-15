import pygame
from pygame.locals import *

class Paddle:
    def __init__(self, screen_width, screen_height, is_player=True):
        self.width = 10
        self.height = 100
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_player = is_player
        self.x = 10 if is_player else screen_width - self.width - 10
        self.y = (screen_height - self.height) // 2
        self.speed = 5

    def move(self, ball=None):
        keys = pygame.key.get_pressed()
        if self.is_player:
            if keys[K_w] and self.y > 0:
                self.y -= self.speed
            if keys[K_s] and self.y + self.height < self.screen_height:
                self.y += self.speed
        else:  # Control the opponent paddle based on the ball's position
            if ball is not None:
                if self.y + self.height // 2 < ball.y and self.y + self.height < self.screen_height:
                    self.y += self.speed
                elif self.y + self.height // 2 > ball.y and self.y > 0:
                    self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def rect(self):
        return (self.x, self.y, self.width, self.height)
