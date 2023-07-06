import apple
import pygame
from constants import *

class Apple_manger:
    def __init__(self):
        self.apples = []
        self.x = GAME_WIDTH
        self.apples.append(apple.Apple())

    def add_apple(self, char):
        self.apples.append(apple.Apple())


    def draw(self, surface):
        for apple in self.apples:
            apple.draw(surface)


    def update(self, char, apple_m):
        for apple in self.apples:
            apple.update(char, apple_m)
