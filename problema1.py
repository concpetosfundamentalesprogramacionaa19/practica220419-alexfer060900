horas = 100
costohora = input("Ingrese por favor el costo hora oficial: ")
        
sueldo = int(costohora) * int(horas)      
descuentoSeguro = int(sueldo*10)/100
sueldocondesc = int(sueldo) - int(descuentoSeguro)

print ("El sueldo del trabajador por sus horas de servicio es de: %s ,"
    "y el descuento del Seguro Social es de: %s\n, por lo tanto," 
    "el total a pagar seria: %s\n" % (sueldo ,descuentoSeguro, sueldocondesc))
    
    
