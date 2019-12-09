import pygame
import random

# GLOBALS VARS
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 650  # meaning 600 // 20 = 20 height per block
block_size = 50
num_row = play_height // block_size
num_column = play_width // block_size

top_left_x = 0
top_left_y = 0
background_color = (0, 0, 0)
_BACKGROUND_COLOR = pygame.Color(0, 0, 0)
shape_colors = {'c1': (0, 255, 0), 'c2': (255, 0, 0), 'c3': (0, 255, 255),
                'c4': (255, 255, 0), 'c5': (255, 165, 0), 'c6': (0, 0, 255), 'c0': (128, 0, 128)}

_COLORS = random.sample(shape_colors.keys(), 3)
_COLUMN = random.sample(range(num_column), 1)[0]

class Piece:
    print('_COLUMN is ', _COLUMN)
    print('_COLORS[0] is ', shape_colors[_COLORS[0]])
    print('_COLORS[1] is ', shape_colors[_COLORS[1]])
    def __init__(self):
        self.x = 0
        self.y = _COLUMN
        self.c0 = shape_colors[_COLORS[0]]
        self.c1 = shape_colors[_COLORS[1]]
        self.c2 = shape_colors[_COLORS[2]]
        self._is_frozen = False
        self._is_done = False


class Columngame:
    def __init__(self):
        self._running = True

    def _create_surface(self, size: (play_width, play_height)) -> None:
        self._surface = pygame.display.set_mode(size)
    def _fill_board(self):
        self._surface.fill(_BACKGROUND_COLOR)

    def create_grid(self):
        grid = [[background_color for x in range(num_column)] for x in range(num_row)]

        print('the function "create_grid"')
        self._grid = grid
        print(self._grid)
        # return grid

    def draw_window(self):
        print('the function "draw_window"')
        self.surface_background = pygame.Surface(self._surface.get_size())
        self.surface_background.fill(background_color)
        # for i in range(num_row):
        #     for j in range(num_column):
        #         pygame.draw.rect(self._surface, self._grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

        # draw grid and border
        # self.draw_grid()
        # pygame.draw.rect(self._surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
        pygame.display.update()

    def draw_grid(self):
        print('the function "draw_grid"')
        sx = top_left_x
        sy = top_left_y
        for i in range(num_row):
            pygame.draw.line(self._surface, (128, 128, 128), (sx, sy + i * block_size),
                             (sx + play_width, sy + i * block_size))  # horizontal lines
            for j in range(num_column):
                pygame.draw.line(self._surface, (128, 128, 128), (sx + j * block_size, sy),
                                 (sx + j * 30, sy + play_height))  # vertical lines

    def convert_shape_format(self):
        temp = self.c0
        self.c0 = self.c1
        self.c1 = self.c2
        self.c2 = temp

    def valid_space(self, grid):
        accepted_positions = [[(j, i) for j in range(num_column) if grid[i][j] == (0, 0, 0)] for i in range(num_row)]
        accepted_positions = [j for sub in accepted_positions for j in sub]
        formatted = convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_positions:
                if pos[1] > -1:
                    return False

        return True

    def check_lost(self, positions):
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False

    def get_shape(self):
        return Piece()

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            self._create_surface((play_width, play_height))
            print(self._surface)
            n = 0
            self._fill_board()
            print(self._surface.fill(_BACKGROUND_COLOR))
            # self.create_grid()
            # self.draw_window()
            # self.draw_grid()

            while self._running:
                clock.tick(15)
                print(n)
                n += 1
                # self._handle_events()
                # self._create_frame()

        finally:
            pygame.quit()


if __name__ == '__main__':
    Columngame().run()