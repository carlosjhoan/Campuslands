#Test_1
#Este programa lee archivos .csv con los registros de temperatura diarios de los diferentes observatorios del país
#Crea un archivo .json que contiene esta información
#Permite además observar los diferentes reportes.

#LIBRERÍAS UTILIZADAS
import json

#VALIDACIONES
#Función del menú principal
def menu(msj):
    while True:
        try:
            opc = int(input(msj))
            if opc < 1 or opc > 7:
                print ("Debe ser un numero de 1 a 6.")
                
                continue
            return opc
        
        except ValueError:
            print ("ERROR !!! Debe ingresar un número entero.")

#ARCHIVOS
#validación del nombre del archivo de registro
def nombre_csv(reg):
    try:
        nomb_reg = reg
        list_nomb = nomb_reg.split("-")
        dia = list_nomb[0].strip()
        if len(dia) < 2 and int(dia) > 0:
            dia = "0" + dia
        else:
            pass
        dia = int(dia)
        mes = list_nomb[1].strip()
        if len(mes) < 2 and int(mes) > 0:
            mes = "0" + mes
        else:
            pass
        year = list_nomb[2].strip()
        list_year = year.split(".")
        year = int(list_year[0])
        return True, dia, mes, year

    except Exception as e:
        print ("""\nEl nombre de este archivo no es el correcto.
               Recuerda que el formato es'dd-mm-aaaa.csv'""")
        return False, "", "", ""


#validación del archivo .csv con los registros:
#INFORMACIÓN IMPORTANTE: El nombre del archivo debe tener el siguiente formato "dia-mes-año.csv"
def verificar_archivo_csv (ruta, reg):
    try:
        lista_reg_dia = []
        observacion = open(ruta, "r")
        
        observacion.close
        return lista_reg_dia

    except Exception as e:
        print (f"\nEl archivo {reg} no corresponde al registro de los observatorios.")

        
    
        



#DESARROLLO DEL PROGRAMA
registro = "02-02-23.csv" #archivo .csv con los registros de temperatura. Su nombre es la fecha del registro [dia-mes-año]
carpeta = "filtro_1"
ruta = f"{carpeta}/{registro}"
while True:
    opc = menu("""MENÚ
               1. Listado de observatorios (por código)
               2. Listado de observatorios (por nombre)
               3. Listado de observaciones de un observatorio
               4. Información de un observatorio
               5. Listado de observaciones a nivel nacional (por código)
               6. Listado de observaciones a nivel nacional (por promedio de temperatura)
               7. SALIR

               >> Indicar opción [1 - 7]: """)
    
    if opc == 1:
        pass

    elif opc == 2:
        pass

    elif opc == 2:
        pass

    elif opc == 2:
        pass

    elif opc == 2:
        pass

    elif opc == 2:
        pass

    else: 
        si_no = input("""\n¿Está seguro que desea salir? 
                      s -- Sí, deseo salir!!
                      n -- No, deseo continuar!!!
                      
                      >>> ¿Opción [s/n]?: """)
        
        if si_no == "s" or si_no == "S":
            print ("\nEsperamos haberle sido de utilidad.")
            input ("\nPresione cualquier tecla para SALIR... ")
            break
        else:
            input ("\nPresione cualquier tecla para volver al menú... ")
            
    

            