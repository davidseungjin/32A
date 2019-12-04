#
# Student ID    : 001037870
# UCInetID      : seungl21
# Name          : Seungjin Lee
#
class Faller:
    def __init__(self, col, color1, color2, color3):
        self.col = col
        self._color1 = color1
        self._color2 = color2
        self._color3 = color3
        self._faller = self._generateFaller()
        self._is_frozen = False
        self._faller_count = 0
        self._done = False

    def getFaller(self) -> list:
        return self._faller

    def getCol(self) -> int:
        return self.col

    def _generateFaller(self) -> list:
        faller = []
        faller.append(self._color1)
        faller.append(self._color2)
        faller.append(self._color3)
        return faller

    def addFrozen(self):
        self._is_frozen = True
