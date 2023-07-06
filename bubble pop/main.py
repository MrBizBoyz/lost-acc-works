import pygame
from constants import *
import bubble_manger

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

bm = bubble_manger.Bubble_manger()

def draw():
    surface.fill((102, 255, 255))
    bm.draw(surface)
    pygame.display.flip()


def update():
    bm.update()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                bm.clicked(pygame.mouse.get_pos())
            if event.type == pygame.QUIT:
                running = False

        draw()
        update()

    pygame.quit()


if __name__ == "__main__":
    main()
