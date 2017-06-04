# -*- coding: utf-8 -*-

calificaciones = {}

calificaciones ['algoritmos'] = 9
calificaciones ['matematicas'] = 10
calificaciones ['web'] = 8
calificaciones ['bases_de_datos'] = 10

#iterar a lo largo de las llaves
for key in calificaciones:
    print(key)

#iterar a lo largo de los valores
for value in calificaciones.values():
    print(value)

#iterar entre las llaves y los valores
for key , value in calificaciones.iteritems():
    print('llave: {}, valor: {}'.format(key, value))
#if __name__ == '__main__':

suma_de_calificaciones = 0

for calificacion in calificaciones.values():
    suma_de_calificaciones +=calificacion

promedio = suma_de_calificaciones /len(calificaciones.values())
print("suma de calificaciones: {}, Promedio: {}".format(suma_de_calificaciones, promedio))
