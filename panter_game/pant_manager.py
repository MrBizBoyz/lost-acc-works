import pygame
from constants import *
import pant

class Pant_manager():

    def __init__(self):
        self.pant = []
        self.fire_rate = 1
        self.now = pygame.time.get_ticks()
        self.last_shot = 0

    def update(self, player):
        print(pygame.time.get_ticks())
        self.key_input(player)
        for b in self.pant:
            b.update()
            if b.can_delete == True:
                self.pant.remove(b)


    def draw(self, surface):
        for b in self.pant:
            b.draw(surface)

    def add_pant(self, player):
        self.pant.append(pant.Pant(player.hit_box.x, player.hit_box.y))

    def key_input(self, player):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:

            self.now = pygame.time.get_ticks()

            if self.now > self.last_shot + self.fire_rate:
                self.add_pant(player)

                self.last_shot = self.now
