x = input("Ingrese el valor de x: ")
y = input("Ingrese el valor de y: ")
z = input("Ingrese el valor de z: ")
        
m = (float (x) + float (y)/float (z))/(float (x) - float (y)/float (z))
        
print("El valor de m, en base a las variables:\n"
    "x = %s\n\t y = %s \n\t\t z = %s\n da como resultado:\n\t\t\t"
    "m = %.1f" % (x,y,z,m))