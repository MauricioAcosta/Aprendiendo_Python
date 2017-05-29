# -*- coding: utf-8 -*-
import random
def run():
    print("Bienvenido al juego adivina el numero aleatorio :D")
    number_end=int(raw_input("Hasta cual numero aleatorio quieres jugar: "))
    number_found = False
    random_number = random.randint(0, number_end)
    while not number_found:
        number = int(raw_input("Intenta un numero: "))
        if number == random_number:
            number_found=True
            print("Felicidades encontraste el numero :D")
        elif number > random_number:
            print("El numero es mas pequeño")
        else:
            print("el numero es mas grande")
if __name__ == '__main__':
    run()
