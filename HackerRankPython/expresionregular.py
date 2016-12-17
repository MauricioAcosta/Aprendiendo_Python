import os
import re
lista=['a3','b3','c3','5','a4']
for numero in range(0,len(lista)):
	if re.match('a[1-5]+',lista[numero]):
		print (numero)
		print (lista[numero])
os.system('ls')
