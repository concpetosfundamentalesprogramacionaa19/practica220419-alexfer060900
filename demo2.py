"""
	Ejemplo de Lenguaje Python
	autor:@alex
"""

import sys

variable = sys.argv[0]
dato1 = sys.argv[1]
dato2 = sys.argv[2]
suma = int(dato1) + int(dato2) # aqui realizo la suma de variables
mult = int(dato1) * int(dato2) # aqui realizo la multiplicacion de variables 

print ("variable argv[0]:	%s" % variable)
print ("variable argv[1]:	%s" % dato1)
print ("variable argv[2]:	%s" % dato2)
print ("La suma es:		%s" % suma)
print ("La multiplicacion es:	 %s" % mult)	 