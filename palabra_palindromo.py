# -*- coding utf-8 -*-

def palindrome(word):
    reversed_word = word[::-1]
    if reversed_word==word:
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
