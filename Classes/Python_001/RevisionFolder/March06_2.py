#main class to call the subclass.

from March06 import printer

def main():

    #lets call the function in the other class
    name='YuvaRaj, this printed from the other class'
    printer(name)
  
if __name__ == '__main__':
    main()
