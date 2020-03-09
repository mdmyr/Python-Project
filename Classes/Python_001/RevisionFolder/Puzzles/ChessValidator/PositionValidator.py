#This Program file will validate a position of the chess board.

'''
1. input is a dictionary, providing a dictionary is out of scope.
2. read the dictionary and display the positions

Logic ::Positions
1. generate the Chess Matrix
2. check the input keys with the values in the matrix.
     if exist : then it is a valid position

Logic:: No of Pawns
1. Check the duplicates  in values.
    if exist it is a invalid entry
2.No. of pawn counts
    pawn : 8
    other : 8

'''
from RevisionFolder.Puzzles.ChessValidator.MatrixTest import createChessMatrixKey


def generateChessMatrix():
    #returns the matrix of the chess board.
    #for 8 row
    chessBoardKey =createChessMatrixKey()
    print(chessBoardKey)



def validatePositions(InputChessPositions):
    #This function will validate the positions.
    # 1. count the pawns both sides , 16 in total, 8 on the pawn
    # 2. positons, should be valid, has to be btw  (number, alpha)


    pass


def ChessPoistionValidator(InputChessPositions):

     print("Check the input type")
     print(type(InputChessPositions))

     #check the input type
     if(isinstance(InputChessPositions, dict)): # isinstance of
      print("Yes")
      validatePositions(InputChessPositions)
      generateChessMatrix()
     else:
         print('Please provide a Validate input')
         return'Invalid input'
if __name__ == '__main__':
    ChessPoistionValidator({'yuvaraj':'The'})
