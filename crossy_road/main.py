from constants import *
import pygame
import char
import car
import car_manger


clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

char = char.Char()
car_m = car_manger.Car_manger()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT :
                    char.move_left()
                if event.key == pygame.K_RIGHT :
                    char.move_right()
                if event.key == pygame.K_UP :
                    char.move_up()
                if event.key == pygame.K_DOWN :
                    char.move_down()

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    char.change_color()

        draw()
        update()

    pygame.quit()


def draw():
    surface.fill((0, 0, 0))
    char.draw(surface)
    car_m.draw(surface)

    pygame.display.flip()


def update():
    char.update()
    car_m.update(char)





if __name__ == "__main__":
    main()
