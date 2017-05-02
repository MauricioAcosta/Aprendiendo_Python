import re

if re.match("python", "python"):
    print "cierto"
if re.match(".ython","python"):
    print "tambien"
if re.match(".ython", "jython"):
    print "tambien 2"
