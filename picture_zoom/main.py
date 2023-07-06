from constants import *
import pygame
import char


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

finn = char.Char()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        draw()
        update()

    pygame.quit()


def draw():
    surface.fill((0, 0, 0))
    finn.draw(surface)
    pygame.display.flip()


def update():
    finn.update()



if __name__ == "__main__":
    main()
