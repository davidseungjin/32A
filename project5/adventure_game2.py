# adventure_game2.py
#
# ICS 32A Fall 2019
# Code Example
#
# This version of our Adventure game added two features:
#
# (1) We replaced the single-colored, rectangular player with an image
#     of a Pekingese instead.
# (2) When the user presses the Enter/Return key, we played a sound of
#     that Pekingese barking.
#
# One big improvemnet I've made here, which we didn't see in lecture,
# is doing less work with the image.  We load the image from a file
# called "gray_peke.png", then scale it (i.e., proportionally change
# its size to fit into the rectangular area where we draw our player).
# But that scaled image is actually the same in every frame, *except*
# when we change the size of the window.  So a better approach, which
# I'm doing here, is to do this:
#
# * Load the image initially and store it.
# * The first time you draw it, scale it once and store the scaled
#   version, as well.
# * Keep the scaled version and, whenever it's available, use it
#   without re-scaling.
# * When the size of the window changes, throw away the scaled version,
#   which will trigger re-scaling the next time we draw a frame.

import adventure
import pygame



_FRAME_RATE = 30
_INITIAL_WIDTH = 600
_INITIAL_HEIGHT = 600
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)



class AdventureGame:
    def __init__(self):
        self._state = adventure.GameState()
        self._running = True


    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            # Load our image, but we haven't got a scaled-down version
            # yet.  We'll scale it when we need it.
            self._player_image = pygame.image.load('gray_peke.png')
            self._player_image_scaled = None

            # Load our barking sound, so we can play it later.
            self._bark_sound = pygame.mixer.Sound('dogbark.wav')

            self._create_surface((_INITIAL_WIDTH, _INITIAL_HEIGHT))
            
            while self._running:
                clock.tick(_FRAME_RATE)
                self._handle_events()
                self._draw_frame()

        finally:
            pygame.quit()


    def _create_surface(self, size: (int, int)) -> None:
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

        # Throw away the scaled version of the player image.  Since the
        # size of the window has changed, we'll need to re-scale it to
        # be appropriate to the window's new size, which we'll do the
        # next time we draw a frame.
        self._player_image_scaled = None


    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._handle_event(event)

        self._handle_keys()


    def _handle_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._stop_running()
        elif event.type == pygame.VIDEORESIZE:
            self._create_surface(event.size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # A pygame.KEYDOWN event with a key attribute pygame.K_RETURN
                # will fire whenever the user presses the Enter/Return key
                # on the keyboard.  In response, we'll play our bark sound.
                self._bark()


    def _handle_keys(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._state.player().move_left()

        if keys[pygame.K_RIGHT]:
            self._state.player().move_right()

        if keys[pygame.K_UP]:
            self._state.player().move_up()

        if keys[pygame.K_DOWN]:
            self._state.player().move_down()


    def _bark(self) -> None:
        # We'll opt for the simple approach of just asking our sound to
        # play, because we know we won't be playing too many of these
        # sounds at once.  If we had more complex needs, we would need
        # to investigate the pygame.mixer library's functionality more
        # carefully.

        self._bark_sound.play()


    def _stop_running(self) -> None:
        self._running = False


    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        self._draw_player()
        pygame.display.flip()


    def _draw_player(self) -> None:
        top_left_frac_x, top_left_frac_y = self._state.player().top_left()
        width_frac = self._state.player().width()
        height_frac = self._state.player().height()

        top_left_pixel_x = self._frac_x_to_pixel_x(top_left_frac_x)
        top_left_pixel_y = self._frac_y_to_pixel_y(top_left_frac_y)
        width_pixel = self._frac_x_to_pixel_x(width_frac)
        height_pixel = self._frac_y_to_pixel_y(height_frac)

        player_rect = pygame.Rect(
            top_left_pixel_x, top_left_pixel_y,
            width_pixel, height_pixel)

        if self._player_image_scaled == None:
            # If we don't have a scaled version of our image, then we'll
            # need to create one.  We do that by calling the
            # pygame.transform.scale() function, which takes two arguments:
            # an image and the size you want the image to be.  The result
            # is an image that has been scaled proportionally, which we'll
            # store in self._player_image_scaled.
            self._player_image_scaled = pygame.transform.scale(
                self._player_image, (width_pixel, height_pixel))

        # Now, we'll draw our scaled image -- either the one we just created
        # or, if we had it already, the one we already had.
        self._surface.blit(
            self._player_image_scaled,
            (top_left_pixel_x, top_left_pixel_y))
            

    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())


    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())


    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)



if __name__ == '__main__':
    AdventureGame().run()
