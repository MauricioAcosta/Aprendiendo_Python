#!/usr/bin/env python
# -*- coding: utf-8 -*


def run():
    counter = 0
    with open('aleph.txt') as f:
        #print(f.readlines())
        for line in f:
            counter += line.count('Aleph')
    print('La palabra Aleph se encuentra {} veces'.format(counter))




if __name__ == '__main__':
    run()
