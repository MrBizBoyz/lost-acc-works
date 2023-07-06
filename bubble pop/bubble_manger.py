#todo:   add bonus round

import bubble
import pygame
class Bubble_manger:
    def __init__(self):
        self.bubbles = []
        self.shots = 15
        for i in range(10):
            self.bubbles.append(bubble.Bubble())

    def draw(self, surface):
        for bub in self.bubbles:
            bub.draw(surface)
    def update(self):
        for bub in self.bubbles:
            bub.update()

    def clicked(self, pos):
        self.shots = self.shots -1



        for bub in self.bubbles:
            if bub.clicked(pos):
                self.bubbles.remove(bub)
        if len(self.bubbles) > self.shots:
            print("game over")
        if self.shots == self.bubbles:
            print("you won")
