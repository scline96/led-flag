import random, sys, time, pygame
from pygame.locals import *
import math

# Constants
FPS = 20            # Frame per second rate of render
MATRIX_PIXEL_SIZE = 10
PIXEL_WIDTH = 32
PIXEL_HEIGHT = 16
WINDOW_WIDTH = PIXEL_WIDTH * MATRIX_PIXEL_SIZE  # Width of window in px
WINDOW_HEIGHT = PIXEL_HEIGHT * MATRIX_PIXEL_SIZE # Height of window in px
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BG_COLOR = BLACK
TEXT_COLOR = WHITE

class Pixel(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pixel = pygame.Rect(self.x * MATRIX_PIXEL_SIZE, self.y * MATRIX_PIXEL_SIZE,
                            MATRIX_PIXEL_SIZE, MATRIX_PIXEL_SIZE)
        pygame.draw.rect(DISPLAY_SURF, self.color, pixel)


def main():
    global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('RGB Led Matrix Testing')

    BASIC_FONT = pygame.font.Font('freesansbold.ttf', 20)
    row_offset = 0
    col_offset = 0
    # Main game loop
    while True:
        check_for_quit()
        DISPLAY_SURF.fill(BLACK)

        # Recreate simulated LED matrix



        # Event handling loop
        for event in pygame.event.get():
            # TODO: improve the feel of the controls
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pass
                elif event.key == K_a:
                    pass
                elif event.key == K_RIGHT:
                    pass
                elif event.key == K_d:
                    pass
            elif event.type == KEYUP:
                pass


        pixel_matrix = [[Pixel(i, j, BLACK)
                         for j in range(PIXEL_HEIGHT)]
                        for i in range(PIXEL_WIDTH)]
        print(col_offset, row_offset)

        pixel_matrix[col_offset][row_offset].color = WHITE
        for i in range(PIXEL_WIDTH):
            for j in range(PIXEL_HEIGHT):
                pixel_matrix[i][j].draw()

        col_offset += 1
        if col_offset >= PIXEL_WIDTH:
            col_offset = 0
            row_offset += 1

        row_offset %= PIXEL_HEIGHT
        print(col_offset, row_offset)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


def terminate():
    pygame.quit()
    # sys.exit()


def check_for_quit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)    # Put key event back in event queue if not ESC key

if __name__ == '__main__':
    main()