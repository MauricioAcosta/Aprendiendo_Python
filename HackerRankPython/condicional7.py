num1=int(input("num1: "))
if num1<=9:
	print("num de una cifra")
	#elif num1<0:
	#	num1=num1*(-1) 
else:	
	if num1<=99:
		print("dos cifras")
	elif num1<=999:	
		print("tres cifras")
	else: 
		print("Error....") 

