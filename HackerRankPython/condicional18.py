contador=1
cantidad=0
num=int(input("Numero de materiales "))
while contador<=num:
    largo=float(input("Ingrese el largo del material ",contador))
    if largo>=1.20 and largo<=1.30:
        cantidad=cantidad+1
    contador=contador+1
print("Cantidad de meteriales seleccionados: ",cantidad)
