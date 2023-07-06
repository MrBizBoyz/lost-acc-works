import pygame, random
from constants import *
import random
pygame.init()

class Cars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 64
        self.speed = 5
        self.x = 0
        self.y = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)








    # def update(self, pgroup):
    #     self.key_input()
    #     # self.collide(cars_group)
    #
    #
    # # def collide(self, cars_group):
    # #
    # #     cars = pygame.sprite.spritecollide(self, cars_group, False)
    # #
    # #     if cars:
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # def key_input(self):
    #
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_LEFT]:
    #
    #         if self.rect.x > 0:
    #             self.rect.x += -self.speed
    #
    #     if keys[pygame.K_RIGHT]:
    #         if self.rect.left < GAME_WIDTH:
    #             self.rect.x += self.speed
