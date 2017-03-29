corX=int(input("Cordenada x: "))
corY=int(input("Cordenada y: "))
if corX!=0 and corY!=0:
	if corX>0 and corY>0:
		print("Cuadrante 1")
	else:	
		if corX<0 and corY>0:
	                print("Cuadrante 2")
		elif corX<0 and corY<0:
                	print("Cuadrante 3")
		elif corX>0 and corY<0:
                	print("Cuadrante 4")
else:
	print("El punto esta sobre los ejes")
