from constants import *
import pygame
import bullet_manager
import enemy_master
import player


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))



p = [
    (0, 0),
    (400, 0),
    (400, 400),
    (0, 0),
    (0, 500),
    (300, 300),
    (800, 800)
]

em = enemy_master.Enemy_master(p)
pygame.init()

player = player.Char()
bm = bullet_manager.Bullet_manager()


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
    surface.fill((255, 255, 255))#background

    em.draw(surface)
    player.draw(surface)
    pygame.display.flip()


def update():
    player.update()


if __name__ == "__main__":
    main()
