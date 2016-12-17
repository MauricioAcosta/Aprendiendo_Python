if __name__ == '__main__':
    entrada= int(input())
    #range() crea una especie de lista (un generador por si quiere leer) que sirve para iterar sobre el
# esto va desde 1 hasta entrada+1 porque el ultimo valor no lo toma
    for numero in range(1,entrada+1):
        print(numero, end="")
