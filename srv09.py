#Validación del menú
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 8:
                print ("Debe ser un numero de 1 a 8.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Validación de horas trabajadas
def horas_trabajadas(msj):
    while True:
        try:
            horas = int(input(msj))
            if horas < 1 or horas > 160:
                print ("\nLa cantidad de horas trabajadas debe estar entre 1 y 160.")
                #input("Presiona una tecla para continuar... ")
                continue
            return horas
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Validación dEl valor de la hora
def valor_hora(msj):
    while True:
        try:
            valor = int(input(msj))
            if valor < 8000 or valor > 150000:
                print ("\nEl valor de la hora debe estar entre $8.000 y $150.000.")
                #input("Presiona una tecla para continuar... ")
                continue
            return valor
        
        except ValueError:
            print ("\nERROR !!! Debe ingresar un número entero.")

#Validación del nombre
def valid_nombre(msj):
    while True:
        try:
            nombre = input(msj)
            if not nombre.isalnum():
                print ("\nEl nombre solo puede contener números y letras.")
                #input("Presiona una tecla para continuar... ")
                continue
            return nombre

        except Exception as e:
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla para continuar... ")

#Validación del ID del empleado
def valid_id(lst, msj):
    while True:
        try:
            a = 0
            id = input(msj)
            if not id.isdigit():
                print ("\nEl ID solo puede contener números.")
                #input("Presiona una tecla para continuar... ")
                continue
            
            for i in lst:
                if i[1] == id:
                    a = 1

            if a == 1:
                print ("\nEste ID no se puede asignar. Ya sen encuentra en la base de datos")
                continue

            print ("ID asignado!!")
            return id

        except Exception as e:
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla pra continuar... ")
#Función permite ingresar ID
def ingresar_id(msj):
    while True:
        try:
            
            id = input(msj)
            if not id.isdigit():
                print ("\nEl ID solo puede contener números.")
                #input("Presiona una tecla para continuar... ")
                continue
            
           

            
            return id

        except Exception as e:
            print ("Ha ocurrido un ERROR!!!")
            input ("Presion una tecla pra continuar... ")

#Empleado a modificar
def modif_empleado(max_n):
    while True:
        try:
            num_empl = int(input("Digite el índice del empleado que desea modificar según la lista anterior. "))
            if num_empl < 1 or num_empl > max_n:
                print (f"\nEl índice del empleado debe estar entre 1 y {max_n}.")
                #input("Presiona una tecla para continuar... ")
                continue
            return num_empl
        except ValueError:
            print ("\nERROR !!! Debe ingresar un número entero.")

#Función que muestra el nombre de los empleados
def nomb_empleados(lst): 
    n = 0
    lst_vac = []
    nom_id = []
    for i in lst:
        n += 1
        nom_id.append(i[0])
        nom_id.append(i[1])
        lst_vac.append(nom_id)
        nom_id = []
        #print (f"{n} -- {i[0]}")
    return lst_vac

#Validación del menú de modificación de la información del empleado
def menu_modif(msj):
    while True:
        try:
            opc = int(input(msj))
            if (opc < 1 or opc > 4):
                print ("Debe ser un numero de 1 a 4.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#Definición salario neto
def nom_empleado (horas, precio_hora):
    sal_minimo = 1160000
    porc_EPS = 0.04
    porc_pens = 0.04
    subs_transporte = 140600
    salario_bruto = precio_hora * horas
    descuentos = (porc_EPS + porc_pens) * salario_bruto
    if salario_bruto <= sal_minimo:
        salario_neto = salario_bruto + subs_transporte - descuentos
    else:
        salario_neto = salario_bruto - descuentos

    return salario_neto, descuentos


    

list_empleados = []
empleado = []

while True:
    opc = menu("""NÓMINA ACME
                    MENÚ

                1 -- Agregar empleado.
                2 -- Modificar empleado.
                3 -- Buscar empleado.
                4 -- Eliminar empleado.
                5 -- Listar empleados.
                6 -- Listar nómina de un empleado.
                7 -- Listar nómina de todos los empleados.
                8 -- SALIR.
                            >>>Elegir una opción [1 - 8]: 
                """)

    if opc == 1:
        print ("\nAGREGAR UN EMPLEADO")
        nombre = valid_nombre("Ingrese el nombre del empleado: ")
        empleado.append(nombre)
        id_empleado = valid_id(list_empleados, "Digite el ID del empleado: ")
        empleado.append(id_empleado)
        hor_trab = horas_trabajadas("Ingrese la cantidad de horas trabajadas por el empleado: ")
        empleado.append(hor_trab)
        val_hora = valor_hora("Ingrese el valor de la hora del empleado: ")
        empleado.append(val_hora)
        list_empleados.append(empleado)
        empleado = []
        #print ("list_empleados : ", list_empleados)
        #print ("empleado : ", empleado)
        input("Presione cualquier tecla para volver al menú... ")

    elif opc == 2:
        print ("\nMODIFICAR EMPLEADO")
        n = 0
        lst_empl = nomb_empleados(list_empleados)
        for i in lst_empl:  
            n += 1
            print (f"{n} -- {i[0]} id: {i[1]}")
        f = len(lst_empl) + 1
        empl_modif = modif_empleado(f)
        pos_empl = empl_modif - 1

        opc_modif = menu_modif("""Qué desea modificar?
                                1 -- Nombre
                                2 -- Cantidad de horas trabajadas
                                3 -- Valor de horas trabajadas
                                4 -- Dejar todo igual""")
        if opc_modif == 1:
            list_empleados[pos_empl][0] =  valid_nombre("Ingrese el nombre del empleado: ")

        elif opc_modif == 2:
            list_empleados[pos_empl][2] =  horas_trabajadas("Ingrese la cantidad de horas trabajadas por el empleado: ")
        
        elif opc_modif == 3:
            list_empleados[pos_empl][3] = valor_hora("Ingrese el valor de la hora del empleado: ")

        else:
            print ("\nTodo quedará igual.")
            pass
        input ("\nPresione cualquier tecla para volver al menú... ")

    
    elif opc == 3:
        print("\nBUSCAR EMPLEADO.")
        id_buscar = ingresar_id("Ingrese el id del empleado que desea buscar: ")
        a = 0
        for i in list_empleados:
            if i[1] == id_buscar:
                print ("\n", "*=" * 30)
                print ("Información del empleado.")
                print (f"Nombre: {i[0]}")
                print (f"ID: {i[1]}")
                print (f"Horas trabajadas: {i[2]}")
                print (f"Valor de la hora: {i[3]}")
                print ( "*=" * 30)
                a = 1

        if a == 0:
            print ("\nEL empleado no se puede encontrar, porque no está agregado a la base de datos")
        input ("\nPresione cualquier tecla para volver al menú... ")

    elif opc == 4:
        print("\nELIMINAR EMPLEADO.")
        id_buscar = ingresar_id("Ingrese el id del empleado que desea eliminar: ")
        a = 0
        for i in list_empleados:
            if i[1] == id_buscar:
                list_empleados.remove(i)
                print (f"\nEl empleado con id {id_buscar} ha sido eliminado.")
                a = 1
            
        if a == 0:
            print ("\nEL empleado no se puede eliminar, porque no está agregado a la base de datos")

        input ("\nPresione cualquier tecla para volver al menú... ")

    elif opc == 5:
        print ("\nLISTAR EMPLEADOS")
        #print (len(list_empleados))
        permiso = "s"
        seguir = "s"
        n = 0
        si_no = ""

        for i in list_empleados:
            if permiso == "s" or permiso == "S":        
                print ("\n", "*=" * 30)
                print ("Información del empleado.")
                print (f"Nombre: {i[0]}")
                print (f"ID: {i[1]}")
                print (f"Horas trabajadas: {i[2]}")
                print (f"Valor de la hora: ${i[3]:,}")
                print ( "*=" * 30)
            
            else:
                pass

            n += 1
            if n == 5:
                si_no = input("""\nDesea continuar listando o parar el programa?
                                    s -- Sí quiero seguir listando
                                    n -- NO quiero seguir listando""")
            if si_no == "s" or si_no == "S":
                n = 0

            elif si_no == "":
                pass 
            else:
                permiso = "n"              
        input ("\nPresione cualquier tecla para volver al menú... ")    

    elif opc == 6:
        print ("\nLISTAR NÓMINA DE UN EMPLEADO") 
        id_buscar = ingresar_id("Ingrese el id del empleado: ")
        a = 0
        for i in list_empleados:
            if i[1] == id_buscar:
                print ("\n", "*=" * 30)
                print ("Información del empleado.")
                print (f"Nombre: {i[0]}")
                print (f"ID: {i[1]}")
                print (f"Horas trabajadas: {i[2]}")
                print (f"Valor de la hora: {i[3]}")
                print (f"Descuentos por EPS y pensión: ${nom_empleado (i[2], i[3])[1]:,.0f}")
                print (f"Nómina: ${nom_empleado (i[2], i[3])[0]:,.0f}")
                print ( "*=" * 30)
                a = 1

        if a == 0:
            print ("\nEL empleado no se puede encontrar, porque no está agregado a la base de datos")
        input ("\nPresione cualquier tecla para volver al menú principal... ")             

    elif opc == 7:
        print ("LISTAR NÓMINA DE TODOS LOS EMPELADOS.")
        nom_total = 0
        for i in list_empleados:
            nom_total += nom_empleado (i[2], i[3])[0]
        print (f"La nómina total de los empleados es: ${nom_total:,.0f}")
        input ("Presione cualquier tecla para volver al menú principal...")
    
    else:
        print ("\nUn gusto poder servirle")
        input ("Presiona cualquier tecla para SALIR... ")
        break