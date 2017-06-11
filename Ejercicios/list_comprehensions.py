# -*- coding: utf-8 -*-

pares = [x for x in range(100) if x % 2 == 0]
print ("numeros pares: ", pares)
nones = [x for x in range(100) if x % 2 != 0]
print ("numeros impares: ",nones)
cuadrados = {x: x**2 for x in range(100)}
print ("numeros cuadrados: ", cuadrados)
