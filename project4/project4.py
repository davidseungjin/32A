#
# Student ID    : 001037870
# UCInetID      : seungl21
# Name          : Seungjin Lee
#
import project4_01 as pm

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