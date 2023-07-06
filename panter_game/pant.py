from constants import *
import pygame


class Pant:
    def __init__(self, x, y):
        self.y = x
        self.x = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.speed = 5
        self.color = YELLOW
        self.hit_box = pygame.Rect(self.y, self.x, self.width, self.height)
        self.can_delete = False



    def update(self):
        if self.hit_box.y + self.hit_box.height  < 0:
            self.can_delete = True

    def draw(self, surface):
        if keys[pygame.K_w]:
            self.color = WHITE

        if keys[pygame.K_b]:
            self.color = BLACK

        if keys[pygame.K_r]:
            self.color = RED

        if keys[pygame.K_b]:
            self.color = BLUE

        if keys[pygame.K_g]:
            self.color = GREEN

        if keys[pygame.K_y]:
            self.color = YELLOW                    
        pygame.draw.rect(surface, self.color, self.hit_box)
