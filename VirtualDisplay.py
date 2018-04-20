import random, sys, time, pygame
from pygame.locals import *
from pygame import freetype
import numpy as np
import math

# Constants
FPS = 20  # Frame per second rate of render
NUM_CHANNELS = 3
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
        # Check if first set of points on screen
        # initialize x and y, otherwise, initialize them to
        if 0 <= x0 <= self.width and 0 <= y0 <= self.height:
            x = x0
            y = y0
        elif 0 <= x0 <= self.width and 0 <= y0 <= self.height:
            x = x1
            y = y1
        else:
            # Clip line if possible
            x_len = x0 - x1
            if x_len:
                pass
            else:
                # Handle vertical case
                pass

        new_slope = 2 * (y1 - y0)
        new_slope_error = new_slope - (x1 - x0)
        x = x0
        y = y0
        while x <= x1 and 0 <= x <= self.width:
            self.screen[x][y].color = line_color
            new_slope_error += new_slope
            if new_slope_error >= 0:
                y += 1
                new_slope_error -= 2 * (x1 - x0)
            x += 1

    def text(self, x, y, text, text_font, text_color=WHITE, bg_color=BLACK):
        byte_string, dim = text_font.render_raw(text)
        dim = dim[1], dim[0]  # Flipping the coord order for numpy
        split_bytes = [int(bool(byte)) for byte in byte_string]
        shaped_bitmap = np.reshape(split_bytes, dim).tolist()
        colored_bitmap = [[text_color if bit else bg_color for bit in row] for row in shaped_bitmap]
        self.image(x, y, colored_bitmap)

    def image(self, x, y, pixels):
        dim = (len(pixels[0]), len(pixels))
        # Check to draw only the portion of the image that is on screen
        for i in range(max(0, -x), min(dim[0], self.width - max(x, 0))):
            for j in range(max(0, -y), min(dim[1], self.height - max(y, 0))):
                # WARNING: screen coordinates are (x, y) img coords are (y, x)
                # since the img "displays" in the console properly this way
                self.screen[x + i][y + j].color = pixels[j][i]

    def points(self, coords, point_color):
        pass


# TODO: game of life
def life(initial=None):
    if initial:
        pass
    else:
        pass


# TODO: Auto-pong
def auto_pong():
    pass


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


# Loading the font
freetype.init()
font = freetype.Font('10x20.bdf')


def main():
    global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('RGB Led Matrix Testing')

    BASIC_FONT = pygame.font.Font('freesansbold.ttf', 20)
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
        pixel_matrix.text(-15, -7, "Test", font)

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
