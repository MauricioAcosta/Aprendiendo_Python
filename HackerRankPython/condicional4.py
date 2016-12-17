num1=int(input("Nota1: "))
num2=int(input("Nota2: "))
num3=int(input("Nota3: "))
promedio=(num1+num2+num3)/3
if promedio>=7:
	print("Promocionado")
else:
	if promedio>=4:
		print("Regular")
	else:
		print("Reprobado")
