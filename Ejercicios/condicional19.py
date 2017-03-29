contador=1
notamayor=0
notamenor=0
while contador<=10:
    print("nota alunmo ",contador)
    nota=int(input())
    if nota>=7:
        notamayor=notamayor+1
    else:
        notamenor=notamenor+1
    contador=contador+1
print("Alunmos con nota>=7 ",notamayor)
print("Alunmos con nota<7 ",notamenor)
