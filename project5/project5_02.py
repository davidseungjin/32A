import project5_faller as pm
import pygame
import random

_FRAME_RATE = 0.5
_LENGTH_ROW = 650
_LENGTH_COLUMN = 300
_NUM_ROW = 13
_NUM_COLUMN = 6
_BLOCK_SIZE = 50

_BACKGROUND_COLOR = pygame.Color(0, 0, 0)

class AdventureGame:
    def __init__(self):
        self._running = True
        self._falling = False
        self._faller_created = False
        self._gameboard = []
        self._validposition = []

    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

    def _create_board(self):
        grid = [[(0, 0, 0) for x in range(_NUM_COLUMN)] for x in range(_NUM_ROW)]
        self._gameboard = grid

    def _valid_position(self):
        _valid_position = [[(j, i) for j in range(6) if self._gameboard[i][j] == (0, 0, 0)] for i in range(13)]
        self._validposition = _valid_position
        print('self._validposition is ', self._validposition)

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)
        self._handle_keys()

    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._stop_running()
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)

    def _stop_running(self) -> None:
        self._running = False

    def _handle_keys(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._player.move_left()
            print('left key')
        if keys[pygame.K_RIGHT]:
            self._player.move_right()
            print('right key')
        if keys[pygame.K_SPACE]:
            self._player.rotate()
            print('space key')

    def _create_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._create_faller()
        # self._falling_faller()
        pygame.display.flip()

    def _create_faller(self) -> None:
        self._player = pm.Faller()
        print('color0 is ', self._player._c0)
        self._faller_created = True

    def _startandfalling(self, _player):
        if _player._row == 0:  # and one more condition: not landed, not blocked
            print('_player._row == 0')
            pass
        if _player._row == 1:  # and one more condition: not landed, not blocked
            print('_player._row == 1')
            pass
        if 2 <= _player._row < self._row:  # and one more condition: not landed, not blocked
            print('_player._row >= 2')
            pass

    def _draw_grid(self):
        self._surface.fill((64, 64, 64))
        for i in range(_NUM_COLUMN):
            pygame.draw.line(self._surface, (128, 128, 128), (0, i * _BLOCK_SIZE),
                             (_BLOCK_SIZE, i * _BLOCK_SIZE))
            for j in range(_NUM_ROW):
                pygame.draw.line(self._surface, (128, 128, 128), (j * _BLOCK_SIZE, 0),
                                 (j * _BLOCK_SIZE, _BLOCK_SIZE))

    def _draw_window(self):
        self._surface.fill((0, 0, 0))
        print('draw_window function ', self._surface.fill((0, 0, 0)))
        for i in range(_NUM_ROW):
            print('i is ', i)
            for j in range(_NUM_COLUMN):
                print('j is ', j)
                pygame.draw.rect(self._surface, self._gameboard[i][j],
                                 (j * _BLOCK_SIZE, i * _BLOCK_SIZE, _BLOCK_SIZE, _BLOCK_SIZE), 0)
                print(pygame.draw.rect(self._surface, self._gameboard[i][j],
                                 (j * _BLOCK_SIZE, i * _BLOCK_SIZE, _BLOCK_SIZE, _BLOCK_SIZE), 0))
        # pygame.draw.rect(self._surface, (255, 0, 0), (0, 0, _LENGTH_COLUMN, _LENGTH_ROW), 15)


    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())

    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)

    def run(self) -> None:
        pygame.init()
        try:
            clock = pygame.time.Clock()
            self._create_surface((_LENGTH_COLUMN, _LENGTH_ROW))
            # create bg color
            # create grid
            self._create_board()
            self._valid_position()
            # create grid line (optional)
            n = 0
            while self._running:
                clock.tick(_FRAME_RATE)
                print(n)
                n += 1
                self._handle_events()
                self._create_frame()
                self._draw_grid()
                self._draw_window()
                self._startandfalling(self._player)
        finally:
            pygame.quit()


if __name__ == '__main__':
    AdventureGame().run()
