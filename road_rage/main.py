from constants import *
import pygame, random
import player_car
import cars


pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

cars_group = pygame.sprite.Group()
player_car_group = pygame.sprite.Group()




player_car = player_car.Player_car()
cars = cars.Cars()


player_car_group.add(player_car)
cars_group.add(cars)










def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()




        draw()
        update()

    pygame.quit()




def draw():
    surface.fill((200, 200, 200))
    player_car_group.draw(surface)
    cars_group.draw(surface)




    pygame.display.flip()


def update():
    player_car_group.update(cars_group)
    cars_group.update()









if __name__ == "__main__":
    main()
