contador=1
suma=0
while contador<=10:
    print("Ingrese el numero ",contador,".")
    num=int(input())
    suma=suma+num
    contador=contador+1
promedio=suma/10
print("Suma: ",suma)
print("Promedio: ",promedio)
