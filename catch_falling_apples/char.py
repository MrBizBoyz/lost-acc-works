from constants import *
import pygame
class Char:
    def __init__(self):
        self.height = 20
        self.width = 175
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT - self.height
        self.speed = 50
        self.color = GREEN
        self.count = 0
        self.color_index = [RED, GREEN, BLUE, (127, 255, 0), (255, 255, 255)]
        self.score = 0


    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.width < GAME_WIDTH:
            self.x += self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
