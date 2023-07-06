from constants import *
import pygame
import random

class Apple:
    def __init__(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.y = -BLOCK_SIZE
        self.x = random.randint(0, GAME_WIDTH  + -BLOCK_SIZE)
        self.speed = 5
        self.color = RED

    def update(self, char, apple_m):
        self.move(char)

        if self.collide(char):

             char.score += 1

             if char.score % 10 == 0:
                 apple_m.add_apple(char)


             self.y = -BLOCK_SIZE
             self.x = random.randint(0, GAME_WIDTH)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, char):
        if self.y > GAME_HEIGHT:
            self.y = -BLOCK_SIZE
            char.score -= 1
        self.y += self.speed


    def collide(self, char):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        char_rect = char.get_rect()
        return rect.colliderect(char_rect)
