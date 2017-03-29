if __name__ == '__main__':
    N = int(input())
    lista=[]
    for i in range(N):
        lee=input().split()
        if lee[0]=="insert":
            lista.insert(int(lee[1]),int(lee[2]))
        elif lee[0]=="print":
            print(lista)
        elif lee[0]=="remove":
            lista.remove(int(lee[1]))
        elif lee[0]=="append":
            lista.append(int(lee[1]))
        elif lee[0]=="sort":
            lista.sort()
        elif lee[0]=="pop":
            lista.pop()
        elif lee[0]=="reverse":
            lista.reverse()
