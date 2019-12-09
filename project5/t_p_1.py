import random
import pygame

shape_colors = {'c1': (0, 255, 0), 'c2': (255, 0, 0), 'c3': (0, 255, 255),
                'c4': (255, 255, 0), 'c5': (255, 165, 0), 'c6': (0, 0, 255), 'c0': (128, 0, 128)}
_NUM_COLUMN = 6
_COLORS = random.sample(shape_colors.keys(), 3)
_COLUMN = random.sample(range(_NUM_COLUMN), 1)[0]

class Piece():
    print('_COLUMN is ', _COLUMN)
    print('_COLORS[0] is ', _COLORS[0])
    print('_COLORS[1] is ', _COLORS[1])
    def __init__(self):
        self.x = 0
        self.y = _COLUMN
        self.c0 = shape_colors(_COLORS[0])
        self.c1 = shape_colors(_COLORS[1])
        self.c2 = shape_colors(_COLORS[2])
        self._is_frozen = False
        self._is_done = False


if __name__ == '__main__':
    a = Piece()