# -*- coding: utf-8 -*-

def factorial(number):
    if number == 0:
        return 1
    #elif number==1:
    #    return number
    return number * factorial(number-1)

def main():
    number = int(raw_input("Ingresa un numero para calcular su factorial: "))
    result = factorial(number)
    print (result)
if __name__ == '__main__':
    main()
