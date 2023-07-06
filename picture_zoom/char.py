from constants import *
import pygame

class Char:
    def __init__(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE

        self.min_width = 10
        self.zoom_speed = 1
        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height
        self.speed = 10

    def update(self):
        self.key_input()

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.width, self.height))

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:#zoom out
            if self.width >= self.min_width:
                self.width -= self.zoom_speed

        if keys[pygame.K_RIGHT]:#zoom in
            self.width += self.zoom_speed

        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass

        if keys[pygame.K_w]:#zoom in
            self.y -= self.speed

        if keys[pygame.K_r]:#zoom in
            self.reset()

    def reset(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE

        self.x = GAME_WIDTH // 2 - self.width // 2
        self.y = GAME_HEIGHT - self.height
