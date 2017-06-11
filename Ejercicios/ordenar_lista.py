# -*- coding: utf-8 -*-
from sys import stdin


def order_list(lista,low,high):

    if high==len(lista) - 1:
        return lista
    print(lista)
    if lista[low]>lista[high]:
        ax=0
        ax=lista[high]
        lista[high]=lista[low]
        lista[low]=ax
        order_list(lista,low+1,high+1)
    print(lista)

if __name__ == '__main__':
    print("Ordena tu lista")
    lista=[]
    while True:
        numbers=stdin.readline().split()
        if numbers != []:
            number=''.join(numbers)
        elif numbers==[]:
            break
        lista.append(int(number))
    print(order_list(lista,0,1))
