# -*- coding: utf-8 -*-
count=0
def binary_search(numbers, number_to_find, low, high):
    count+=1
    if low > high:
        return False
    mid = (low + high) / 2
    count+=1
    if numbers[mid]== number_to_find:
        return True
    count+1
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low,mid-1)
    else:
        return binary_search(numbers, number_to_find, mid+1, high)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(raw_input('Ingresa un número: '))

    result, count = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    if result is True:
        print('EL numero esta en la lista :D')
        print('Intentos ',count)
    else:
        print('El numero no esta en la lista')
        print('Intentos ',count)