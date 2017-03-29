num=int(input("numero positivo de uno o dos digitos (1..99) "))
if num<=9:
	print("Numero de un digito")
elif num>=10 and num<=99:
	print("Numero de dos digitos")
else:
	print("No Corresponde a un numero de uno ni de dos digitos")
