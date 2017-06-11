import re

if re.match("python", "python"):
    print "cierto"
if re.match(".ython","python"):
    print "tambien"
if re.match(".ython", "jython"):
    print "tambien 2"

if re.match("...\.","abc."):
    print "la cadena consste en 3 caracreres segidos"
if re.match("python|jython|cython", "python"):
    print "solo para python|jython|cython"
if re.match("[pjc]ython","python"):
    print "encerrar caracteres"
if re.match("python[0-9]","python0"):
    print "comprobar si la cadena es “python0” , “python1” ,“python2” , ... , “python9”"
if re.match("python[0-9a-zA-Z]","pythonp"):
    print "último carácter fuera o un dígito o una letra"
if re.match("python[^0-9a-z]", "python+"):
    print "no nos interesa que comience por python"

