contador=1
sumaaltura=0
numalturas=int(input("Ingrese el num de personas "))
while contador<=numalturas:
    print("Altura persona ",contador)
    altura=float(input())
    sumaaltura=sumaaltura+altura
    promedioAltura=sumaaltura/numalturas
    contador+=1
print("Promedio de altura de",numalturas,"personas es: ",promedioAltura)
