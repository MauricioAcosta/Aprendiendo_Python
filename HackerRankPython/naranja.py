#!/usr/bin/python
# -*- coding: utf-8 -*-
def jugar(intento=1):
    respuesta = raw_input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print "\nFallaste! Inténtalo de nuevo"
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print "\nPerdiste!"
    else:
        print "\nGanaste!"
jugar()


