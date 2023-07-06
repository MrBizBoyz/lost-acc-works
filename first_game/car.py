from constants import *
import pygame

class Char:
    def __init__(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height
        self.speed = 10
        self.color = RED
        self.count = 0


    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
