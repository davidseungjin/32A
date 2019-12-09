import project5_faller
import pygame

# We'll define some global constants, to introduce names for what would
# otherwise be "magic numbers" in our code.  Naming constant values with
# something that says what they're going to be used for is a good habit
# to get into.  (People read programs, and it helps if they understand
# the "why" of those programs.)

_FRAME_RATE = 2
_LENGTH_ROW = 650
_LENGTH_COLUMN = 300
_NUM_ROW = 13
_NUM_COLUMN = 6

_BACKGROUND_COLOR = pygame.Color(255, 255, 255)
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
        # self._state = project5_faller.GameState()
        self._running = True

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            self._create_surface((_LENGTH_COLUMN, _LENGTH_ROW))

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

    def _stop_running(self) -> None:
        self._running = False

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
            # self._state.player().move_left()
            print('left key')

        if keys[pygame.K_RIGHT]:
            # self._state.player().move_right()
            print('right key')

        if keys[pygame.K_SPACE]:
            # self._state.player().move_down()
            print('space key')

    def _draw_frame(self) -> None:
        self._surface.fill(_BACKGROUND_COLOR)
        # self._draw_player()
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

'''
import project5_faller as pm

class ColumnGame:
    def __init__(self, user_column, user_row, user_option='EMPTY'):
        self._running = True
        self._matched = False
        self._column = user_column
        self._row = user_row
        self._option = user_option
        self._gameboard = []

    def getColumn(self) -> int:
        return self._column

    def getRow(self) -> int:
        return self._row

    def getBoard(self) -> [[str]]:
        if self._option == 'EMPTY':
            return self._EmptyBoard()
        elif self._option == 'CONTENTS':
            return self._ContentsBoard()

    def _setBoard(self, newsetting):
        self._gameboard = newsetting

    def _EmptyBoard(self):
        myboard = []
        for col in range(self._row):
            myboard.append([])
            for row in range(self._column):
                myboard[-1].append('   ')
        self._option = 'CONTENTS'
        return myboard

    def _ContentsBoard(self):
        if self._gameboard != []:
            return self._gameboard
        return self._InitialBoard()

    def _InitialBoard(self):
        mylist = []
        for n in range(self._row):
            mysublist = []
            myinput = input()
            while len(myinput) != self._column:
                myinput = input()
            for i in myinput:
                mysublist.append(i)
            for i in range(len(mysublist)):
                mysublist[i] = ' ' + mysublist[i] + ' '
            mylist.append(mysublist)
        self._setBoard(mylist)
        self._fill_the_hole_recursion()
        return mylist

    def _displayBoard(self):
        self._gameboard = self.getBoard()
        for space in self._gameboard:
            d = []
            for tile in space:
                d.append(tile)
            print('|' + ''.join(d) + '|')
        print(' ' + '-' * 3 * self.getColumn() + ' ')

    def _fill_the_hole_recursion(self):
        for i in range(self._row-1):
            self._fill_the_hole()

    def _fill_the_hole(self):
        display = self._gameboard
        for i in range(self._row -1, -1, -1):
            for j in range(self._column-1, -1, -1):
                if i > 0:
                    try:
                        if display[i][j] == '   ' and display[i-1][j] != '   ':
                            display[i][j] = display[i-1][j]
                            display[i-1][j] = '   '
                    except:
                        continue
        self._setBoard(display)

    def rotateFaller(self, block):
        if block._done != True:
            temp = block._faller[0]
            block._faller[0] = block._faller[1]
            block._faller[1] = block._faller[2]
            block._faller[2] = temp
            i = min(self._row - 1, block._faller_count-1)
            display = self._gameboard
            if i == 0:
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            if i == 1:
                display[i - 1][int(block.col) - 1] = '[' + block._faller[1] + ']'
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            if 2 <= i < self._row:
                for tomakeblank in range(i - 2):
                    display[tomakeblank][int(block.col) - 1] = '   '
                display[i - 2][int(block.col) - 1] = '[' + block._faller[0] + ']'
                display[i - 1][int(block.col) - 1] = '[' + block._faller[1] + ']'
                display[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            self._setBoard(display)

    def _moveLeft(self, block):
        i = min(self._row - 1, block._faller_count-1)
        if (int(block.col) -1) > 0 and block._is_frozen == False:
            if i == 0 and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i + 1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1
            if i == 1 \
                    and self._gameboard[i-1][int(block.col) - 2] == '   ' \
                    and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i + 1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1
            if 2 <= i < self._row -1\
                    and self._gameboard[i-2][int(block.col) - 2] == '   ' \
                    and self._gameboard[i-1][int(block.col) - 2] == '   ' \
                    and self._gameboard[i][int(block.col) - 2] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col)-1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) - 1

    def _moveRight(self, block):
        i = min(self._row - 1, block._faller_count-1)
        if (int(block.col) - 1) < (self._column - 1) and block._is_frozen == False:
            if i == 0 and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1
            if i == 1 \
                    and self._gameboard[i - 1][int(block.col)] == '   ' \
                    and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1
            if 2 <= i < self._row -1 \
                    and self._gameboard[i - 2][int(block.col)] == '   ' \
                    and self._gameboard[i - 1][int(block.col)] == '   ' \
                    and self._gameboard[i][int(block.col)] == '   ':
                for n in range(i+1):
                    self._gameboard[n][int(block.col) - 1] = '   '
                block._faller_count -= 1
                block.col = int(block.col) + 1

    def _match(self):
        display = self._gameboard
        for i in range(self._row - 1, -1, -1):
            for j in range(self._column - 1, -1, -1):
                target = display[i][j][1]
                if target != ' ':
                    try:
                        if display[i+1][j][1] == target and display[i+2][j][1] == target:
                            display[i+1][j] = '*' + target + '*'
                            display[i+2][j] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    try:
                        if display[i][j+1][1] == target and display[i][j+2][1] == target:
                            # print('row match case: left to right')
                            display[i][j+1] = '*' + target + '*'
                            display[i][j+2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    try:
                        if display[i-1][j-1][1] == target and display[i-2][j-2][1] == target and i >= 2 and j >= 2:
                            display[i-1][j-1] = '*' + target + '*'
                            display[i-2][j-2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
                    try:
                        if display[i-1][j+1][1] == target and display[i-2][j+2][1] == target and i >= 2:
                            display[i-1][j+1] = '*' + target + '*'
                            display[i-2][j+2] = '*' + target + '*'
                            display[i][j] = '*' + target + '*'
                            self._matched = True
                    except:
                        pass
        self._setBoard(display)

    def _eliminate_matched(self):
        'Traget and marking only'
        display = self._gameboard
        for i in range(self._row - 1, -1, -1):
            for j in range(self._column - 1, -1, -1):
                if display[i][j][0] == '*':
                    display[i][j] = '   '
        self._setBoard(display)
        self._fill_the_hole_recursion()
        self._matched = False

    def startandfalling(self, block):
        i = min(self._row - 1, block._faller_count)
        if i == 0 and self._gameboard[i][int(block.col)-1] == '   ':
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1
        if i == 1 \
                and self._gameboard[i][int(block.col)-1] == '   ':
            self._gameboard[i-1][int(block.col) - 1] = '[' + block._faller[1] + ']'
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1
        if 2 <= i < self._row \
                and self._gameboard[i][int(block.col) - 1] == '   ':
            for tomakeblank in range(i-2):
                self._gameboard[tomakeblank][int(block.col) - 1] = '   '
            self._gameboard[i-2][int(block.col) - 1] = '[' + block._faller[0] + ']'
            self._gameboard[i-1][int(block.col) - 1] = '[' + block._faller[1] + ']'
            self._gameboard[i][int(block.col) - 1] = '[' + block._faller[2] + ']'
            block._faller_count += 1

    def landing(self, block):
        try:
            if block._faller_count == self._row or self._gameboard[block._faller_count][int(block.col) - 1] != '   ':
                if block._faller_count == 1:
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                if block._faller_count == 2:
                    self._gameboard[block._faller_count - 2][int(block.col) - 1] = '|' + block._faller[1] + '|'
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                if block._faller_count > 2:
                    self._gameboard[block._faller_count - 3][int(block.col) - 1] = '|' + block._faller[0] + '|'
                    self._gameboard[block._faller_count - 2][int(block.col) - 1] = '|' + block._faller[1] + '|'
                    self._gameboard[block._faller_count - 1][int(block.col) - 1] = '|' + block._faller[2] + '|'
                block.addFrozen()
        except:
            pass

    def _checkBlock(self, block):
        if block._is_frozen:
            self._gameboard[block._faller_count - 3][int(block.col) - 1] = ' ' + block._faller[0] + ' '
            self._gameboard[block._faller_count - 2][int(block.col) - 1] = ' ' + block._faller[1] + ' '
            self._gameboard[block._faller_count - 1][int(block.col) - 1] = ' ' + block._faller[2] + ' '
            block._done = True

    def run(self):
        myinput = ''
        self._displayBoard()
        myinput = input()
        while (self._running) and (myinput != 'Q'):
            self._match()
            if self._matched == True:
                self._displayBoard()
                mytempinput = input()
                self._eliminate_matched()
                self._displayBoard()
            if myinput != '' and myinput != 'Q' and myinput != '<' and myinput != 'R' and myinput != '>':
                block = pm.Faller(myinput[2], myinput[4], myinput[6], myinput[8])
                self.startandfalling(block)
                self._displayBoard()
                while block._done != True:
                    mysubinput = input()
                    if mysubinput =='':
                        self.startandfalling(block)
                        self.landing(block)
                        self._displayBoard()
                        self._checkBlock(block)
                        if block._done == True:
                            mysubinput = input()
                            self._displayBoard()
                    if mysubinput == 'R':
                        self.rotateFaller(block)
                        self._displayBoard()
                    if mysubinput == '<':
                        self._moveLeft(block)
                        self.startandfalling(block)
                        self._displayBoard()
                    if mysubinput == '>':
                        self._moveRight(block)
                        self.startandfalling(block)
                        self._displayBoard()
            try:
                if block._faller_count < 3 and block._done == True:
                    self._running = False
            except:
                pass
            myinput = input()
        if myinput != 'Q':
            print("GAME OVER")


    def _end_game(self) -> bool:
        if block._faller_count >= 3:
            return False
        return True

if __name__ == '__main__':
    user_row = int(input())
    user_column = int(input())
    gamestatus = input()

    mygame = ColumnGame(user_column, user_row, gamestatus)
    mygame.run()
'''