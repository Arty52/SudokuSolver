#Art Grichine
#ArtGrichine@gmail.com

import sys

class Board:
    def __init__(self, puzzle):
        cells = []
        for c in puzzle:
            cells.append(Cell(c))
        
        rows = []
        for r in range(0,81,9):
            rows.append(MyRow(cells[r:r+9]))
        
        cols = []
        for col in range(9)
            this_col = []
            for c in range(col,81,9)
                this_col.append(cells[c])
            cols.append(this_col)
            
        subboard = []
        for x in range(0,81,27):
            for i in range(0,9,3):
                for r in range(0,27,9)
                    subboard.append(MySubBoard(cells[r+i+x:r+i+x+3]))
  
class Cell:
    def __init__(self, item):
        self._item = item
        
    def setMyRow(self, row):
        self._myrow = row
    def getMyRow(self):
        return self._myrow
    myrow = property(getMyRow, setMyRow)
        
    def setMyCol(self, col):
        self._mycol = col
    def getMyCol(self):
        return self._mycol
    mycol = property(getMyCol, setMyCol)
        
    def setMySubBoard(self, sub):
        self._mysubboard = sub
    def getMySubBoard(self):
        return self.mysubboard
    mysubboard = property(getMySubBoard, setMySubBoard)
    

class MyRow:
    def __init__(self, cells):
        myCells = set(cells)
        for cell in myCells:
            cell.myrow = self

class MyCol:
    def __init__(self, cells):
        myCells = set(cells)
        for cell in myCells:
            cell.mycol = self

class MySubBoard:
    def __init__(self, cells):
        myCells = set(cells)
        for cell in myCells:
            cell.mysubboard = self

def main():
    with open(sys.argv[1]) as fh:     #implicitly open and close the file
        for i in fh:
            puzzle = i.rstrip()
            print(i)
        
        
        
    


if __name__ == '__main__':
    main()