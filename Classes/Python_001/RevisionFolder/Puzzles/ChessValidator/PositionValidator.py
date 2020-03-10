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


def exits(find, inList):
    status =True
    if find in inList.keys():

        pass
    else:
        status=False
    return  status


def generateChessMatrix(list):
    #returns the matrix of the chess board.
    status=''
    print("generates a matrix for the chess boxes")
    chessPositions= (createChessMatrixKey())

    for key in list.keys():
        print(key)
        status= exits(key,chessPositions)
        if status==False:
            return False
        else :return True

def validatePositions(InputChessPositions):
    #This function will validate the positions.
    # 1. count the pawns both sides , 16 in total, 8 on the pawn
    # 2. positons, should be valid, has to be btw  (number, alpha)
    status=generateChessMatrix(InputChessPositions)
    print('Chess Board Status ::',status)


def ChessPoistionValidator(InputChessPositions):

     print("Check the input type")
     print(type(InputChessPositions))
     print(InputChessPositions.keys())

     #check the input type
     if(isinstance(InputChessPositions, dict)): # isinstance of
      print("Yes")
      validatePositions(InputChessPositions)
     else:
         print('Please provide a Validate input')
         return'Invalid input'
if __name__ == '__main__':
    ChessPoistionValidator({'1A': '', '1B': '', '1B ': '', '1D': '', '1E': '', '1F': '', '1G': '', '1H': '', '2A': ''})
