import pygame
from pygame.locals import *

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 10
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x = 5
        self.speed_y = 5
        self.reset()

    def reset(self):
        self.x = self.screen_width // 2
        self.y = self.screen_height // 2
        self.speed_x *= -1

    def update(self, player_paddle, opponent_paddle):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with top and bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen_height:
            self.speed_y *= -1

        # Ball collision with paddles
        if pygame.Rect(*self.rect()).colliderect(player_paddle.rect()) and self.speed_x < 0:
            self.speed_x *= -1
        if pygame.Rect(*self.rect()).colliderect(opponent_paddle.rect()) and self.speed_x > 0:
            self.speed_x *= -1

    def check_score(self):
        return self.x < 0 or self.x > self.screen_width

    def out_of_bounds(self):
        if self.x < 0:
            return 'left'
        elif self.x > self.screen_width:
            return 'right'

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

    def rect(self):
        return (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
