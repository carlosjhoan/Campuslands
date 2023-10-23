"Este programa liquida de manera automática la comisión de N conductores de la Empresa TRASRAPIDO. "

nombre = input("ingrese el nombre del conductor: ")
ced = int(input("ingrese la cedula: "))
clas_cond = int(input("""ingrese el tipo de conductor: 
                     1 -- Experto
                     2 -- Novato
                      """))

pas_mes = int(input("ingrese la cantidad recibida por pasajes en el mes: "))
enc_mes = int(input("ingrese la cantidad recibida por encomiendas en el mes: "))

permiso = True
cant_exp = 0 #Cantidad de conductores expertos
cant_nov = 0 #Cantidad de conductores novatos
valor_total_pag = 0 #Valor total a pagar

while permiso == True:

    if clas_cond == 1:
        pag_cond = 0.3 * pas_mes + 0.2 * enc_mes
        cant_exp += 1
        valor_total_pag += pag_cond

    elif clas_cond == 2:
        pag_cond = 0.2 * pas_mes + 0.15 * enc_mes
        cant_nov += 1
        valor_total_pag += pag_cond

    print ("\n", "*=" * 20)
    print (f"Nombre del conductor: {nombre}")
    print (f"Cédula: {ced}")
    print (f"Pago del conductor: {pag_cond:,}")
    print (f"Pago Total a los conductores: {valor_total_pag:,}")
    print (f"N° de expertos: {cant_exp}\tN° de novatos: {cant_nov}")
    print ( "*=" * 20)

    i = input(""""\nContinuar con otro conductor: 
           s -- Sí
           n -- No""")

    if i == "s" or i == "S":
        nombre = input("ingrese el nombre del conductor: ")
        ced = int(input("ingrese la cedula: "))
        clas_cond = int(input("""ingrese el tipo de conductor: 
                     1 -- Experto
                     2 -- Novato
                      """))
        pas_mes = int(input("ingrese la cantidad recibida por pasajes en el mes: "))
        enc_mes = int(input("ingrese la cantidad recibida por encomiendas en el mes: "))
    
    elif i  == "n" or i == "N":
        permiso = False




