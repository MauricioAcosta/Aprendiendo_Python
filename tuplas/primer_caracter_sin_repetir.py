#!/usr/bin/env python
# -*- coding: utf-8 -*

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for index, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] =(index,1)
        else:
            seen_letters[letter] = (seen_letters[letter][0],seen_letters[letter][1]+1)
    print("Diccionario de palabras: {}".format(seen_letters))
    final_letters = []
    for key, value in seen_letters.iteritems():
        if value[1] == 1:
            final_letters.append((key, value[0]))
    print("Lista de tuplas de palabras que no se repiten: {}".format(final_letters))
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

#def sort_order(value): = lambda value: value[1]
#    return value[1]
if __name__ == '__main__':

    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
