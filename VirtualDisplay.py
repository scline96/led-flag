import random, sys, time, pygame
from pygame.locals import *
import math

# Constants
FPS = 20  # Frame per second rate of render
MATRIX_PIXEL_SIZE = 10
PIXEL_WIDTH = 64
PIXEL_HEIGHT = 32
WINDOW_WIDTH = PIXEL_WIDTH * MATRIX_PIXEL_SIZE  # Width of window in px
WINDOW_HEIGHT = PIXEL_HEIGHT * MATRIX_PIXEL_SIZE  # Height of window in px
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BG_COLOR = BLACK
TEXT_COLOR = WHITE

# Yes, I know I'm recreating basic graphics rendering,
# and this stuff has already been implemented thousands of times


class Pixel(object):
    def __init__(self, x, y, pixel_color):
        self.x = x
        self.y = y
        self.color = pixel_color

    def draw(self):
        pixel = pygame.Rect(self.x * MATRIX_PIXEL_SIZE, self.y * MATRIX_PIXEL_SIZE,
                            MATRIX_PIXEL_SIZE, MATRIX_PIXEL_SIZE)
        pygame.draw.rect(DISPLAY_SURF, self.color, pixel)


class PixelMatrix(object):
    def __init__(self, width, height):
        self.screen = [[Pixel(i, j, BLACK)
                        for j in range(height)]
                       for i in range(width)]
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                self.screen[i][j].draw()

    def reset(self):
        self.screen = [[Pixel(i, j, BLACK)
                        for j in range(self.height)]
                       for i in range(self.width)]

    def set_pixel(self, x, y, pixel_color):
        self.screen[x][y].color = pixel_color

    def line(self, x0, y0, x1, y1, line_color=WHITE):
        # Implementation of Bresenham's line algorithm. (See Wikipedia)
        # TODO: Textured line
        new_slope = 2 * (y1 - y0)
        new_slope_error = new_slope - (x1 - x0)
        x = x0
        y = y0
        while x <= x1:
            self.screen[x][y].color = line_color
            new_slope_error += new_slope
            if new_slope_error >= 0:
                y += 1
                new_slope_error -= 2 * (x1 - x0)
            x += 1


def scrolling_pixel(pix_matrix, pixel_color=WHITE):
    col_offset = 0
    row_offset = 0
    while True:
        # Inefficient, but works
        pix_matrix.reset()
        pix_matrix.set_pixel(col_offset, row_offset, pixel_color)
        col_offset += 1
        if col_offset >= pix_matrix.width:
            col_offset = 0
            row_offset += 1
        row_offset %= pix_matrix.height
        yield pix_matrix


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
    matrix = PixelMatrix(PIXEL_WIDTH, PIXEL_HEIGHT)
    scroll_effect = scrolling_pixel(matrix, (125, 27, 43))
    while True:
        check_for_quit()
        DISPLAY_SURF.fill(BLACK)

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

        pixel_matrix = next(scroll_effect)
        pixel_matrix.line(10, 10, 20, 15, (16, 232, 78))
        pixel_matrix.draw()

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
        pygame.event.post(event)  # Put key event back in event queue if not ESC key


if __name__ == '__main__':
    main()
