from constants import *
import pygame
import char
import apple_manger

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

char = char.Char()
apple_m = apple_manger.Apple_manger()


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

                # if event.key == pygame.K_q :
                #     apple_m.add_apple(char)
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
    apple_m.draw(surface)
    draw_scores()

    pygame.display.flip()


def update():
    char.update()
    apple_m.update(char, apple_m)

def draw_scores():
    message_display(str(char.score), GAME_WIDTH // 2 - FONT_SIZE, FONT_SIZE, FONT_SIZE)


def text_objects(text, font):
    textSurface = font.render(text, True, WIHTE)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)




if __name__ == "__main__":
    main()
