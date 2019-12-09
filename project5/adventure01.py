# adventure.py
#
# ICS 32A Fall 2019
# Code Example
#
# This module comprises the "model" for our Adventure game.  Because
# we didn't take the game very far, the model is simple: It consists
# of a rectangular-shaped player, which we can move in any of the
# four basic directions (up, down, left, and/or right).  When the
# player exits one side of the screen, it appears on the opposite
# side of the screen.


_PLAYER_WIDTH = 0.2
_PLAYER_HEIGHT = 0.2
_PLAYER_SPEED = 0.01


# An object of the Player class represents the player.  The only thing
# we presently keep track of is the player's position on the screen,
# which we do by tracking two things: the top-left corner of the
# player's rectangular area and the "size" of the player (i.e., a
# width and a height).
#
# In this version, we're using constant values to represent the width
# and the height, but by making the information available publicly only
# by calling a method in the Player class, we leave open the possibility
# that players might have different widths and heights at different times.

class Player:
    def __init__(self):
        # We want the player to begin centered within the window.
        # To do that, we need the center of the player to be at the
        # fractional coordinate (0.5, 0.5).  However, since what we're
        # tracking is the top-left corner of the player, we'll need to
        # calculate that, by subtracting half the player's width and
        # half the player's height, respectively, from 0.5.
        top_left_x = 0.5 - _PLAYER_WIDTH / 2
        top_left_y = 0.5 - _PLAYER_HEIGHT / 2

        self._top_left = (top_left_x, top_left_y)


    def top_left(self) -> (float, float):
        return self._top_left


    def width(self) -> float:
        return _PLAYER_WIDTH


    def height(self) -> float:
        return _PLAYER_HEIGHT


    # The thing about moving is that it's really the same thing in
    # all four directions: adjust the x- and y-coordinates by some
    # amount, then see if it's necessary to "wrap around" to the
    # other side of the screen.  So notice that all four of the
    # public move methods simply call a private method called _move()
    # that does the actual work, so the fiddly details are handled
    # in one place.

    def move_left(self) -> None:
        self._move(-_PLAYER_SPEED, 0)


    def move_right(self) -> None:
        self._move(_PLAYER_SPEED, 0)


    def move_up(self) -> None:
        self._move(0, -_PLAYER_SPEED)


    def move_down(self) -> None:
        self._move(0, _PLAYER_SPEED)


    def _move(self, delta_x: float, delta_y: float) -> None:
        # What we're given are "deltas" (i.e., by how much should the
        # x- and y-coordinates change?).  First, we'll figure out what
        # the new x- and y-coordinates should be.

        tl_x, tl_y = self._top_left

        new_x = tl_x + delta_x
        new_y = tl_y + delta_y

        # Now that we've figured that out, we'll see if we've moved too
        # far, which we'll define as the center of the player having moved
        # off the edge of the screen.  For example, if the center of the
        # player has moved beyond the left edge of the screen, then we
        # want the player to "wrap around" to the right edge of the screen
        # instead.
        #
        # To do that, we'll first need to figure out the player's center
        # coordinate, which we can do by adding half of the player's width
        # and half of the player's height, respectively, to the new
        # x- and y-coordinates.  If the resulting x-coordinate is negative,
        # we've gone too far to the left; if it's greater than 1, we've
        # gone too far to the right.  The y-coordinate, similar, can be
        # checked to see if we've gone too far up or down.
        #
        # If we've gone too far, we'll adjust by either adding 1 or
        # subtracting 1 from the coordinate, which has the effect of
        # moving the player to the opposite edge of the screen, but
        # at a distance away from that edge that corresponds to the
        # amount by which the player had moved too far.

        half_width = self.width() / 2
        half_height = self.height() / 2

        if new_x + half_width < 0.0:
            new_x += 1.0
        elif new_x + half_width > 1.0:
            new_x -= 1.0

        if new_y + half_height < 0.0:
            new_y += 1.0
        elif new_y + half_height > 1.0:
            new_y -= 1.0

        # Now that we've figured out where the player should be,
        # we store that back into the _top_left attribute.
        
        self._top_left = (new_x, new_y)


# Note, overall, that we made a tradeoff here that may or may not have been
# a good one.  We chose to store the top-left coordinate of the player's
# position.  This made one thing simpler: When the "view" needed to ask about
# the top-left coordinate, we could return it.  That simplicity came at
# the cost of making something else more difficult: Moving the player
# required knowing about the player's center coordinate, instead, which
# we had to calculate on the fly.
#
# An alternative approach would have been to store the center coordinate
# instead.  We would then have had to calculate the top-left when we needed
# it, but could otherwise use the center in places where we needed that.




# An object of the GameState class represents the overall state of our
# entire game.  Because we never evolved past the point where we had a
# player we could move around, the only thing in our GameState class
# is a Player object.  As we extend the game, of course, this class would
# grow.

class GameState:
    def __init__(self):
        self._player = Player()


    def player(self) -> Player:
        return self._player
