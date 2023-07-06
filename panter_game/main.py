from constants import *
import pygame
import pant_manager
import player


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


player = player.Char()
pm = pant_manager.Pant_manager()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background

    player.draw(surface)
    pm.draw(surface)
    pygame.display.flip()


def update():

    player.update()
    pm.update(player)


if __name__ == "__main__":
    main()
