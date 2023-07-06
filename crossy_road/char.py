from constants import *
import pygame

class Char:
    def __init__(self):
        self.height = BLOCK_SIZE
        self.width = BLOCK_SIZE
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT - self.height
        self.speed = 10
        self.color = GREEN
        self.count = 0
        self.color_index = [RED, GREEN, BLUE, (127, 255, 0), (255, 255, 255)]

    def update(self):
        self.key_input()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y > 0:
            self.y -=BLOCK_SIZE
    def move_down(self):
        if self.y + self.height < GAME_HEIGHT:
            self.y +=BLOCK_SIZE
    def move_left(self):
        if self.x > 0:
            self.x -=BLOCK_SIZE

    def move_right(self):
        if self.x + self.width < GAME_WIDTH:
            self.x +=BLOCK_SIZE

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            self.speed = 20
            self.height = 10
            self.width = 30
            self.color = (152, 116, 63)


    def set_loc(self, x, y):
        self.x = x
        self.y = y
