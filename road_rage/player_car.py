import pygame, random
from constants import *
import random
pygame.init()

class Player_car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 64
        self.speed = 5
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT // 2
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)








    def update(self, platform_group):
        self.key_input()


    # def collide(self, platform_group):
    #
    #     platforms = pygame.sprite.spritecollide(self, platform_group, False)
    #
    #     if platforms:
    #         self.rect.bottom = platforms[0].rect.top
    #         self.falling = False
    #     else:
    #         self.rect = self.rect.move(0, self.speed)








    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            if self.rect.x > 0:
                self.rect.x += -self.speed

        if keys[pygame.K_RIGHT]:
            if self.rect.left < GAME_WIDTH:
                self.rect.x += self.speed
