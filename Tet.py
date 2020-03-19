import pygame
import random

pygame.font.init()

# Global Variables
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# Shape Formats

S = [['.....', '.....', '..OO.', '.OO..', '.....'],
     ['.....', '..O..', '..OO.', '...O.', '.....']]

Z = [['.....', '.....', '.OO..', '..OO.', '.....'],
     ['.....', '..O..', '.OO..', '.O...', '.....']]

I = [['..O..', '..O..', '..O..', '..O..', '.....'],
     ['.....', 'OOOO.', '.....', '.....', '.....']]

O = [['.....', '.....', '.OO..', '.OO..', '.....']]

J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'], [
    '.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]

L = [['.....', '...O.', '.OOO.', '.....', '.....'], ['.....', '..O..', '..O..', '..OO.', '.....'], [
    '.....', '.....', '.OOO.', '.O...', '.....'], ['.....', '.OO..', '..O..', '..O..', '.....']]

T = [['.....', '..O..', '.OOO.', '.....', '.....'], ['.....', '..O..', '..OO.', '..O..', '.....'], [
    '.....', '.....', '.OOO.', '..O..', '.....'], ['.....', '..O..', '.OO..', '..O..', '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represents shape


class Piece(object):   # *
    pass


def create_grid(locked_pos={}):   # *
    pass


def convert_shape_format():
    pass


def valid_space():
    pass


def check_lost():
    pass


def get_shape():  # *
    pass


def draw_text_middle():
    pass


def draw_grid():   # *
    pass


def clear_rows():
    pass


def draw_next_shape():
    pass


def draw_window():   # *
    pass


def main():   # *
    pass


def main_menu():   # *
    pass


main_menu()
