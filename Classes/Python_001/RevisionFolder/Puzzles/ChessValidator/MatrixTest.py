
#new key words
#ord -->convert the char to number
#chr -- > number  to char


def createChessMatrixKey():
    #for 8 row
    i =1
    chessBoxKey={}# a dictionary
    chessBoxList=[] #lis to of keys
    while (i <= 8):
       # print(i)
        print('\n')
        j=1
        incr='A'

        while(j <= 8):

            matrixPosition= str(i)+incr
            incr=chr(ord(incr)+1) # convert int to string
           # print(matrixPosition)
            chessBoxList.append(matrixPosition)

            j=j+1
        i=i+1
    #print(chessBoxList)

    chessBoxKey= {element :''  for element in chessBoxList}
    chessBoxKey.update(chessBoxKey)
    print(chessBoxKey)
    return  chessBoxKey

if __name__ == '__main__':
    createChessMatrixKey()
