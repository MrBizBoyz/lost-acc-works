from constants import *
import pygame
import random

class Car:
    def __init__(self, row):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.x = random.randint(0, GAME_WIDTH)
        self.y = row * BLOCK_SIZE
        self.speed = 5
        self.color = RED
        self.count = 0
        self.color_index = [RED, GREEN, BLUE, (127, 255, 0), (255, 255, 255)]

    def update(self, char):
        self.move()

        if self.collide(char):
            char.set_loc(GAME_WIDTH // 2, GAME_HEIGHT - self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.x == -self.width:
            self.x = GAME_WIDTH
        self.x -= self.speed

    def collide(self, char):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        char_rect = char.get_rect()
        return rect.colliderect(char_rect)
