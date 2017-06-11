#!/usr/bin/env python
# -*- coding: utf-8 -*
from lampara import LamparaDeEscritorio

def run():

    lamp = LamparaDeEscritorio(is_turned_on=False)

    while True:
        command = str(raw_input('''
        ¿Que deseas hacer?
        [p]render
        [a]pagar
        [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            print('Hasta luego')
            break
        else:
            print('comando incorrecto')


if __name__ == '__main__':
    run()
