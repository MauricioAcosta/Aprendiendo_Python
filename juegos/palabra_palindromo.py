# -*- coding utf-8 -*-
#!/usr/bin/env python
def palindrome2(word):#forma alternativa
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)
    reversed_word=''.join(reversed_letters)
    if reversed_word == word:
        return True
    else:
        return False

def palindrome(word):#Una mejor forma y mas facil
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Bienvendo al juego de palindromo")
    word = str(raw_input("Escribe una palabra: "))
    result = palindrome(word)
    if result is True:
        print("La palabra {} es palindromo".format(word))
    else:
        print("La palabra {} no es palindromo".format(word))
