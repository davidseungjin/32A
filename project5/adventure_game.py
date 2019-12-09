# adventure_game.py
#
# ICS 32A Fall 2019
# Code Example
#
# This is the very skeletal beginning of an implementation of a game
# called Adventure from 1980.  In Adventure, you control a single-colored,
# rectangular-shaped player, which you move around the screen by manipulating
# a joystick -- or, in our case, by holding down the arrow keys on the
# keyboard instead.
#
# Still we were mainly interested in becoming acclimated to handling
# keyboard inputs, we didn't take the game very far; all we can do is
# move the player around the screen with the arrow keys.  But this got
# us into a few things that we needed in PyGame, which will be of use to
# you in Project #5.

import adventure01
import pygame



# We'll define some global constants, to introduce names for what would
# otherwise be "magic numbers" in our code.  Naming constant values with
# something that says what they're going to be used for is a good habit
# to get into.  (People read programs, and it helps if they understand
# the "why" of those programs.)

_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 0, 255)
_PLAYER_COLOR = pygame.Color(0, 0, 128)



# We'll use the same basic pattern that we used in our previous example,
# which is a pretty nice way to organize a PyGame-based game, but that
# still keeps separate parts of it separate.  Rather than one giant
# game loop that includes everything, we're instead breaking our game
# down into separate methods that handle events, draw our frame, and
# so on.
#
# Since a lot of what was done below is similar to the previous example,
# I'll mostly use comments to illustrate what's new here.

class AdventureGame:
    def __init__(self):
        self._state = adventure01.Player()
        self._running = True


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
            
            while self._running:
                clock.tick(_FRAME_RATE)
                self._handle_events()
                self._draw_frame()

        finally:
            # We've put the call to pygame.quit() into a "finally"
            # block to ensure that it will be called even if an exception
            # causes our game to terminate.  If we successfully called
            # pygame.init() before, then we want to be sure that we
            # call pygame.quit() on the way out.
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


    def _handle_keys(self) -> None:
        # pygame.key.get_pressed() returns something that you can think of
        # as a dictionary that maps keys to boolean values that specify
        # whether those keys are currently being held down.  In other
        # words, we simultaneously find out the current state of every key
        # on the keyboard.

        keys = pygame.key.get_pressed()

        # It's important that we don't use "elif" in each case below,
        # because we want it to be possible to move both left and up
        # at the same time (so that holding two directions down will
        # trigger diagonal movement).  That's why I left a blank line
        # between each of the "if" statements: to make that structure
        # clearer.  (I prefer code that looks like what it is.)

        if keys[pygame.K_LEFT]:
            self._state.move_left()

        if keys[pygame.K_RIGHT]:
            self._state.move_right()

        if keys[pygame.K_UP]:
            self._state.move_up()

        if keys[pygame.K_DOWN]:
            self._state.move_down()


    def _stop_running(self) -> None:
        self._running = False


    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_player()
        pygame.display.flip()


    def _draw_player(self) -> None:
        # We want to draw the player as a rectangle filled with a single
        # color.  The color itself is a global constant _PLAYER_COLOR
        # that's defined near the top of this file.
        #
        # The biggest problem we have is figuring out where to draw the
        # rectangle.  What the "model" can tell us about the player are
        # three things: (1) the top-left fractional coordinate of the
        # player, (2) the player's width (fractionally), and (3) the
        # player's height (fractionally).
        #
        # Because we'll do a fair amount of converting between fractional
        # and pixel coordinates, we've created some helper methods below
        # that can perform those conversions.  We've also named our
        # local variables carefully, so we always know whether we've
        # got a fractional or a pixel coordinate -- something that's
        # otherwise easy to get wrong.
        
        top_left_frac_x, top_left_frac_y = self._state.top_left()
        width_frac = self._state.width()
        height_frac = self._state.height()

        top_left_pixel_x = self._frac_x_to_pixel_x(top_left_frac_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(top_left_frac_y)
        width_pixel = self._frac_x_to_pixel_x(width_frac)
        height_pixel = self._frac_y_to_pixel_y(height_frac)

        player_rect = pygame.Rect(
            top_left_pixel_x, top_left_pixel_y,
            width_pixel, height_pixel)

        # Now that player_rect contains a rectangle where the player
        # should be drawn, all we need to do is fill it with the
        # appopriate color.  The pygame.draw.rect() function can
        # do that for us.

        pygame.draw.rect(self._surface, _PLAYER_COLOR, player_rect)


    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())


    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())


    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)



if __name__ == '__main__':
    AdventureGame().run()
