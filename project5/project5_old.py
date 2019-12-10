import project5_faller as pm
import pygame
import random

# We'll define some global constants, to introduce names for what would
# otherwise be "magic numbers" in our code.  Naming constant values with
# something that says what they're going to be used for is a good habit
# to get into.  (People read programs, and it helps if they understand
# the "why" of those programs.)

_FRAME_RATE = 1
_LENGTH_ROW = 650
_LENGTH_COLUMN = 300
_NUM_ROW = 13
_NUM_COLUMN = 6
_UNIT_FRAC_COORDINATE_COLUMN = _LENGTH_COLUMN / _NUM_COLUMN
_UNIT_FRAC_COORDINATE_ROW = _LENGTH_ROW / _NUM_ROW

_COLOR1 = pygame.Color(0, 0, 128)
_COLOR2 = pygame.Color(0, 0, 64)
_COLOR3 = pygame.Color(0, 128, 0)
_COLOR4 = pygame.Color(0, 64, 0)
_COLOR5 = pygame.Color(128, 0, 0)
_COLOR6 = pygame.Color(64, 0, 0)
_COLOR7 = pygame.Color(64, 64, 64)

_BACKGROUND_COLOR = pygame.Color(0, 0, 0)
_PLAYER_COLOR = pygame.Color(0, 0, 128)



class AdventureGame:
    def __init__(self):
        # self._state = project5_faller.Faller()
        self._running = True
        self._falling = False
        self._faller_created = False

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            self._create_surface((_LENGTH_COLUMN, _LENGTH_ROW))
            n = 0
            while self._running:
                clock.tick(_FRAME_RATE)
                print(n)
                n += 1
                self._handle_events()
                self._create_frame()

        finally:
            pygame.quit()


    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)


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
        self._falling_faller()
        pygame.display.flip()

    def _create_faller(self) -> None:
        _MY_TOTAL_COLORS = (_COLOR1, _COLOR2, _COLOR3, _COLOR4, _COLOR5, _COLOR6, _COLOR7)
        _COLORS = random.sample(_MY_TOTAL_COLORS, 3)
        _COLUMN = random.sample(range(_NUM_COLUMN), 1)[0]

        if self._falling == False:
            self._player = pm.Faller()
            print('self._player created')
            print('color0 is ', self._player._c0)
            print('self._faller_created is in _falling before change', self._faller_created)
            self._faller_created = True


    def _falling_faller(self):
        if self._faller_created == True and (self._player._bottom_topleft[1] < (_NUM_ROW -1)/_NUM_ROW):
            print('((_NUM_ROW-1)/_NUM_ROW) is ', ((_NUM_ROW-1)/_NUM_ROW))
            print('self._player._bottom_topleft[1] is ', self._player._bottom_topleft[1])
            print('self._faller_created is in _falling_faller', self._faller_created)
            self._falling = True
            bottom_topleft_frac_x, bottom_topleft_frac_y = self._player.bottom_topleft()
            middle_topleft_frac_x, middle_topleft_frac_y = self._player.middle_topleft()
            top_topleft_frac_x, top_topleft_frac_y = self._player.top_topleft()
            width_frac = self._player.width()
            height_frac = self._player.height()

            bottom_topleft_pixel_x = self._frac_x_to_pixel_x(bottom_topleft_frac_x)
            bottom_topleft_pixel_y = self._frac_y_to_pixel_y(bottom_topleft_frac_y)
            middle_topleft_pixel_x = self._frac_x_to_pixel_x(middle_topleft_frac_x)
            middle_topleft_pixel_y = self._frac_y_to_pixel_y(middle_topleft_frac_y)
            top_topleft_pixel_x = self._frac_x_to_pixel_x(top_topleft_frac_x)
            top_topleft_pixel_y = self._frac_y_to_pixel_y(top_topleft_frac_y)
            width_pixel = self._frac_x_to_pixel_x(width_frac)
            height_pixel = self._frac_y_to_pixel_y(height_frac)

            player_rect2 = pygame.Rect(
                bottom_topleft_pixel_x, bottom_topleft_pixel_y,
                width_pixel, height_pixel)
            player_rect1 = pygame.Rect(
                middle_topleft_pixel_x, middle_topleft_pixel_y,
                width_pixel, height_pixel)
            player_rect0 = pygame.Rect(
                top_topleft_pixel_x, top_topleft_pixel_y,
                width_pixel, height_pixel)

            pygame.draw.rect(self._surface, self._player._color2, player_rect2)
            pygame.draw.rect(self._surface, self._player._color1, player_rect1)
            pygame.draw.rect(self._surface, self._player._color0, player_rect0)
            print('self._player.bottom_topleft() is ', self._player.bottom_topleft())
            # if (not ((pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]
            #         or pygame.key.get_pressed()[pygame.K_SPACE]))):
            self._player.natural_falling()
        if(self._player._bottom_topleft[1] > 1):
            self._faller_created = False
            self._falling = False

    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())

    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())

    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)


if __name__ == '__main__':
    AdventureGame().run()
