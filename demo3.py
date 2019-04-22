"""
Se procede a ingresar dos datos por teclado y a realizar su suma 
y multiplicacion.
"""

print ("Ingrese el primer valor: ") # Se ingresa el primer valor
dato1 = input()
 
print ("Ingrese el segundo valor: ") # Se ingresa el segundo valor 
dato2 = input()

suma = int(dato1) + int(dato2) # aqui realice la suma de variables
mult = int(dato1) * int(dato2) # aqui realice la multiplicacion de variables 

print ("La suma es:		%s\tLa multiplicacion es:	%s" % (suma, mult)) 
# Se presenta la suma y la multiplicacion de las variables en una sola linea. 