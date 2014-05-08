#Art Grichine
#ArtGrichine@gmail.com

import sys
import queue

#notes:
# #priority que
# s = []          #list acts just like a stack; has pop/push
# q = queue.PriorityQueue()
# 
# for c in cells:
#     if len(c.choices) == 1: #choices is a property
#     #solve
#     elif len(c.choices) > 1:
#         t = (len(c.choices), c)
#         q.put(t)
# 
# cellWeWantToGuessWith = q.get()[1]
# stateOfBoard = str(board)      
# for choice in cellWeWantToGuessWith.choices:
#     t = (cellWeWantToGuessWith.index, choice, stateOfBoard)       #must have index property
#     s.push(t)
# 
# guess = s.pop()
# b.reinit(guess[2])
# b.guess(guess[0],guess[1])

def solve(board):
    universe = list(range(1,10))
    u = set(universe)
    guess = intersection(u, board.rows, board.cols, board.subboard)
    # print(guess)
    
def intersection(universe, row, col, sub):
    return universe - row - col - sub
        
class Board:
    def __init__(self, puzzle):
        self.cells = []
        self._puzzle = puzzle
        for c in puzzle:
            self.cells.append(Cell(c))
        
        self.rows = []
        for r in range(0,81,9):
            self.rows.append(MyRow(self.cells[r:r+9]))
            
        self.cols = []
        for col in range(9):
            this_col = []
            for c in range(col,81,9):
                this_col.append(self.cells[c])
            self.cols.append(MyCol(this_col))
            
        self.subboard = []
        for x in range(0,81,27):
            for i in range(0,9,3):
                for r in range(0,27,9):
                    self.subboard.append(MySubBoard(self.cells[r+i+x:r+i+x+3]))   
                    
    def __str__(self):
        return str(self._puzzle)
            # return ''.join([str(c) for c in cells])
            # m = map(lambda x:str(x), cells)           #same as above but this is map object
#             return ''.join(list(m))
             
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
    
    def __str__(self):
        return str(self._item)

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
        
        print()
        print(puzzle)
        print()
        newBoard = Board(puzzle)
        print(newBoard)
        solve(newBoard)
        # print()
        # print(solver.intersection(newBoard))
        #         
    


if __name__ == '__main__':
    main()