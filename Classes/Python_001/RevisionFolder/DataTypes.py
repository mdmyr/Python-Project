#list of datatypes for reference.


def main():
    name='yuvaraj'
    names=['yuvaraj','raghunapu']
    namePairs={'yuvaraj':'Mahathii'}
    nameDictionary=('Super','Machi')
    rawname= b'super'
    setName=set([3,4,56,6])


    print(name)
    print(name.isalnum())
    print(type(name))
    print(type(names))
    print(type(namePairs))
    print(type(nameDictionary))
    print(type(rawname))
    print(type(setName))
if __name__=='__main__':
    main()


'''
Output
-----
yuvaraj
True
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'tuple'>
<class 'bytes'>
<class 'set'>

'''
