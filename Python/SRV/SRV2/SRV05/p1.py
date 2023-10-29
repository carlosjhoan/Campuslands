"Lista de vendedores de una empresa"

ced = int(input("ingrese la cedula: "))
nombre = input("ingrese el nombre del vendedor: ")
tip_vend = int(input("""ingrese el tipo de vendedor: 
                     1 -- Puerta a puerta
                     2 -- Telemercadeo
                     3 -- Ejecutivo de ventas
                     """))

venta_vend = int(input("ingrese la venta del mes del vendedor: "))

comis_total = 0
ventas_total = 0

while ced != -1:
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

    ced = int(input("ingrese la cedula: "))

    if ced == -1:
        continue

    else:
        nombre = input("ingrese el nombre: ")
        tip_vend = int(input("""ingrese el tipo de vendedor: 
                     1 -- Puerta a puerta
                     2 -- Telemercadeo
                     3 -- Ejecutivo de ventas
                     """))

        venta_vend = int(input("ingrese la venta del mes del vendedor: "))



