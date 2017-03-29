import os
import re
patron = re.match('a[3-5]+',"a3")
if patron:
   print "la palabra esta dentro del patron de expresion regular"
else: 
   print "la palabra no esta"
