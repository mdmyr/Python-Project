
#new key words
#ord -->convert the char to number
#chr -- > number  to char


def createChessMatrixKey():
    #for 8 row
    i =1
    chessBoxKey={}
    while (i <= 8):
       # print(i)
        print('\n')
        j=1
        incr='A'

        while(j < 8):
            #print(i,j)
            #print(chr(ord(incr)+1))
            #print(i,chr(ord(incr)+1))
            incr=chr(ord(incr)+1) # convert int to string
            matrixPosition= str(i)+incr
            print(matrixPosition)
            j=j+1
        i=i+1




if __name__ == '__main__':
    createChessMatrixKey()
