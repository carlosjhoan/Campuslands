#Este programa realiza el cálculo del sueldo neto de cada uno de los vendedores de una empresa.

"Lista de vendedores de una empresa"
#Validacion de la cédula

while True:

    try:
        ced = (input("ingrese la cedula: "))
        if ced.isdigit() != True and ced != '-1':
            print ("Deben ser solo numeros")
            continue
        
        break

    except Exception as e:
        print ("Se ha presentado un error:", e)




comis_total = 0
ventas_total = 0

while ced != '-1':

#validación del nombre

    while True:
        try:
            nombre = input("ingrese el nombre del vendedor: ")
            if nombre.isalnum() !=True:
                print ("El nombre debe ser de solo letras y números")
                continue
            break
        except Exception as e:
            print ("Se ha presentado un erro:", e)


#Validación del tipo de vendedor

    while True:
        try:
            tip_vend = int(input("""ingrese el tipo de vendedor: 
                     1 -- Puerta a puerta
                     2 -- Telemercadeo
                     3 -- Ejecutivo de ventas
                     """))
            if tip_vend < 1 or tip_vend >3:
                print ("Valor fuera del rango. Debe ser, 1, 2 o 3")
                continue
            break
        except ValueError:
            print ("Deben ser un nuúmero entero.\n")        
#Validación del valor de la venta del mes del vendedor

    while True:
        try:
            venta_vend = int(input("ingrese la venta del mes del vendedor: "))
            if venta_vend < 0:
                print ("La venta no puede ser negativa\n")
                continue
            break

        except ValueError:
            print ("Solo se permite la entrada de valores enteros")


    if tip_vend == 1:
        comis_vend = 0.2 * venta_vend
        comis_total += comis_vend
        ventas_total += venta_vend

    elif tip_vend == 2:
        comis_vend = 0.15 * venta_vend
        comis_total += comis_vend
        ventas_total += venta_vend


    elif tip_vend == 3:
        comis_vend = 0.25 * venta_vend
        comis_total += comis_vend
        ventas_total += venta_vend

    print ("\n", "*=" * 35)
    print (f"Nombre del vendedor: {nombre}")
    print (f"Comisión del vendedor: {comis_vend:,}")
    print (f"Comisiones totales: {comis_total:,}")
    print (f"Ventas totales: {ventas_total:,}")
    print ("\n", "*=" * 35)

    #Validacion de la cédula

    while True:

        try:
            ced = (input("ingrese la cedula: "))
            if ced.isdigit() != True and ced != '-1':
                print ("Deben ser solo numeros")
                continue
            break

        except Exception as e:
            print ("Se ha presentado un error:", e)

    
