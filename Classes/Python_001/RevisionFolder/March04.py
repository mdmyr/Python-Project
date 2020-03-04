# March04
# updates

# using the blackslash

def main():
    print('Simple start print')
    #example of the 'backslash'

    a =  1 \
        +1 \
        +5 \
        +6

    print('The total can be %d : ' %(a))

# if ,elif  and else.

    disaster =False
    volcano = False

    if(disaster):
        print('Something to worry about!!')
    elif(volcano):
        print('Rush to safety')
    else:
        print('Have some fun')


#list using for the validation

    list=[]
    if(list.__len__()==0):
        print('list is empty')
    else:
        print('not empty')


#set comparision
    setC = {'b','ab','b,'}
    print(type(setC))
    setC.add('sUPER')
    print(type(setC))
    print(setC)
if __name__ == '__main__':
    main()
