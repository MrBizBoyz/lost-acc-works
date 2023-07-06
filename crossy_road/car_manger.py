import car
import pygame
from constants import *
class Car_manger:
    def __init__(self):
        self.cars = []
        self.x = GAME_WIDTH

        for i in range(9):


            self.cars.append(car.Car(i))

    def draw(self, surface):
        for car in self.cars:
            car.draw(surface)
    def update(self, char):
        for car in self.cars:
            car.update(char)
