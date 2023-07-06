import pygame
from constants import *
import random
class Bubble:
    def __init__(self):
            self.width = 60
            self.height = 60
            self.x =
            self.y 

            self.x_vel = 2
            self.y_vel = 2


    def draw(self, surface):
        pygame.draw.ellipse(surface, GREEN, self.rect)


    def move(self):
        if self.rect.x < 0:
             self.x_vel = -self.x_vel
        if self.rect.x > GAME_WIDTH - self.rect.width:
            self.x_vel = -self.x_vel
        if self.rect.y < 0:
             self.y_vel = -self.y_vel
        if self.rect.y > GAME_HEIGHT - self.rect.height:
             self.y_vel = -self.y_vel

    def update(self):
        self.move()





    def clicked(self, pos):
        return(self.rect.collidepoint(pos))
