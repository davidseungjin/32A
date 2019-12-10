#######################################
# Student ID    : 001037870
# UCInetID      : seungl21
# Name          : Seungjin Lee
#######################################

import random

_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255),  (255, 255, 255),  (128, 128, 128)]


class Faller(object):
    def __init__(self):
        self.x = 0
        self.y = random.sample(range(6),1)[0]
        self.x_m = self.x - 1
        self.x_t = self.x_m - 1
        self.color0 = random.sample(_COLORS, 1)[0]
        self.color1 = random.sample(_COLORS, 1)[0]
        self.color2 = random.sample(_COLORS, 1)[0]

    def faller_rotate(self):
        temp = self.color0
        self.color0 = self.color1
        self.color1 = self.color2
        self.color2 = temp