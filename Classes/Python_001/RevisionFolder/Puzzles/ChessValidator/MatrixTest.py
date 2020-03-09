
#new key words
#ord -->convert the char to number
#chr -- > number  to char


def createChessMatrixKey():
    #for 8 row
    i =1
    #chessBoxKey={}
    while (i <= 8):
        # print(i)
        #print('\n')
        j=1
        incr='A'
        keys=''
        while(j <= 8):
            matrixPosition= str(i)+incr
            incr=chr(ord(incr)+1)
            keys = keys.__add__(str(matrixPosition + ' '))
            j=j+1
        i=i+1

        #print(keys.rstrip().lstrip())

    #adding the values
        chessBoxKey= {value : ' ' for value in keys.lstrip().rstrip().split(' ')}
        print(chessBoxKey)
       # return chessBoxKey

if __name__ == '__main__':
    createChessMatrixKey()
