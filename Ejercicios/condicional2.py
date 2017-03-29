nota1=int(input("Nota1: "))
nota2=int(input("Nota2: "))    
nota3=int(input("Nota3: "))
promedio=(nota1+nota2+nota3)/3
if promedio>=3:
	print("Aprovado ", promedio)
else: 
	print("Reprovado: ", promedio)
