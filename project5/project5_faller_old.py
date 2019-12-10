import pygame
import random

shape_colors = {'c1': (0, 255, 0), 'c2': (255, 0, 0), 'c3': (0, 255, 255),
                    'c4': (255, 255, 0), 'c5': (255, 165, 0), 'c6': (0, 0, 255), 'c0': (128, 0, 128)}

_COLORS = random.sample(shape_colors.keys(), 3)
_COLUMN = random.sample(range(6), 1)[0]             # Column is assigned as 6

class Faller:


    print('_COLUMN is ', _COLUMN)
    print('_COLORS[0] is ', shape_colors[_COLORS[0]])
    print('_COLORS[1] is ', shape_colors[_COLORS[1]])

    def __init__(self):
        self._row = 0
        self._column = _COLUMN
        self._c0 = shape_colors[_COLORS[0]]
        self._c1 = shape_colors[_COLORS[1]]
        self._c2 = shape_colors[_COLORS[2]]
        self._is_frozen = False
        self._is_done = False
        self._block_dimension = 50

    def bottom_position(self) -> (int, int):
        return (self._column, self._row)

    def width(self) -> int:
        return self._block_dimension

    def height(self) -> int:
        return self._block_dimension

    def move_left(self) -> None:
        # print('self._col before moving left is ', self._col)
        self._column = self._column - 1
        # print('self._col after moving left is ', self._col)

    def move_right(self) -> None:
        # print('self._col before moving right is ', self._col)
        self._column = self._column + 1
        # print('self._col after moving right is ', self._col)

    def rotate(self) -> None:
        temp = self._c0
        self._c0 = self._c1
        self._c1 = self._c2
        self._c2 = temp

    def natural_falling(self):
        if self._row < 13:      #  or below block is empty
            self._row += 1
        # print('self._bottom_topleft in natural_falling function is ', self._bottom_topleft)
        # print('after: self._middle_topleft ', self._middle_topleft)
        # print('after: self._top_topleft ', self._top_topleft)
    def _is_Landed(self):
        self._is_frozen = True
