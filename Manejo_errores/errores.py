#!/usr/bin/env python
# -*- coding: utf-8 -*

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'pero': 31
}


while True:
    country = str(raw_input('Escribe el nombre de un país: ')).lower()
    try:
        print('la población de {} es: {} millones.'.format(country, countries[country]))

    except KeyError:
        print('No tenems el dato de la población de {}'.format(country))
