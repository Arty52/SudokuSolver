row column sub-board classes
9x9 colums and rows
81 total cells
numbers 1-9

  3      4       5     6       7
------=====================------
4     |     |       |     |
------=====================------
5     |     |       |     |
------=====================------
6     |     |       |     |
------=====================------
7


Cell
parent class will make:
    myRow
    myCol
    mySubBoard
    
    symbol (value or number in the box)
    
myCol --> Col (each have 9 pointers)            myRow --> Row             mySubBoard --> SubBoard
myCells (these are sets)                        myCells                   myCells
(list)                                          (list)                    (list)

Initialized with 81 cells, Some initialized with values, others with null character (0).

Board:
    list of Cells
    list of Rows
    list of Cols
    list of SubBoards

Methods for column/row/sub_board:
    Routine that tells us whats missing from column/row/sub_board
        intersection of routine above will give us unique symbol

priority que:
    behaves like a list
    insert tuple into list containing cell and number of choices
    
save board like string before guessing (.) to represent empty and continue, if wrong then 
re-initialize pre-guess state and continue onward.



using with in python:
def main():
    with open('puzzles.txt') as fh:
        blah
        blah
        blah
        
with will implicitly open and close the file.