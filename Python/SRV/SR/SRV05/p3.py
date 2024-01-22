"Program que se encarga de liquidar los honorarios de los docentes"

id = input("ingrese el documento de identidad: ")
nombre = input("ingrese el nombre del docente: ")
cat_docente = (input("""ingrese la categoría del docente: 
                     A 
                     B 
                     C 
                     """))
horas_trab = int(input("ingrese las horas trabajadas: "))


total_pag = 0 #Total a pagar a todos los docentes
cant_A = 0
cant_B = 0
cant_C = 0

i = True
while i == True:
    if cat_docente == "A" or cat_docente == "a":
        hon_doc = 25000 * horas_trab
        total_pag += hon_doc
        cant_A += 1

    elif cat_docente == "B" or cat_docente == "b":
        hon_doc = 35000 * horas_trab
        total_pag += hon_doc
        cant_B += 1


    elif cat_docente == "C" or cat_docente == "C":
        hon_doc = 50000 * horas_trab
        total_pag += hon_doc
        cant_C += 1

    print ("\n", "*=" * 20)
    print (f"Nombre del docente: {nombre}")
    print (f"Documento de identidad: {id}")
    print (f"Honorarios del docente: {hon_doc:,}")
    print (f"Pago total de honorarios: {total_pag:,}")
    print (f"N° de A: {cant_A}",f"\nN° de B: {cant_B}", f"\nN° de C: {cant_C}")
    print ( "*=" * 20)

    a = input(""""\nContinuar con otro conductor: 
           s -- Sí
           n -- No""")

    if a == "s" or a == "S":
        id = input("ingrese el documento de identidad: ")
        nombre = input("ingrese el nombre del docente: ")
        cat_docente = (input("""ingrese la categoría del docente: 
                     A 
                     B 
                     C 
                     """))
        horas_trab = int(input("ingrese las horas trabajadas: "))
    
    elif a  == "n" or a == "N":
        i = False












