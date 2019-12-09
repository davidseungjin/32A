import random
import pygame

shape_colors = {'c1':(0, 255, 0), 'c2':(255, 0, 0), 'c3':(0, 255, 255),
                'c4':(255, 255, 0), 'c5':(255, 165, 0), 'c6':(0, 0, 255), 'c7':(128, 0, 128)}
_NUM_COLUMN = 6
_COLORS = random.sample(shape_colors.keys(), 3)
_COLUMN = random.sample(range(_NUM_COLUMN), 1)[0]
print('_COLUMN is ', _COLUMN)

class Piece:  # *
    print('_COLUMN is ', _COLUMN)
    print('_COLORS[0] is ', _COLORS[0])
    print('_COLORS[1] is ', _COLORS[1])
    def __init__(self):
        self.x = 0
        self.y = _COLUMN
        self.color_b = _COLORS[0]
        self.color_m = _COLORS[1]
        self.color_t = _COLORS[2]
        # self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0