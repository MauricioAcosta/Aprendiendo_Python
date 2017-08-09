# -*- coding: utf-8 -*-
def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False
    mid = (low + high) / 2

    if numbers[mid]== number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid-1)

    else:
        return binary_search(numbers, number_to_find, mid+1, high)


if __name__ == '__main__':

    #numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    numbers_in = raw_input("Ingresa una lista separada por espacio: ").split()
    numbers=[]
    for i in numbers_in:
        numbers.append(int(i))

    number_to_find = int(raw_input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    if result is True:
        print('EL numero esta en la lista :D')
    else:
        print('El numero no esta en la lista')
