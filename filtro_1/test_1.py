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
        mes = list_nomb[1].strip()
        if len(mes) < 2 and int(mes) > 0:
            mes = "0" + mes
        else:
            pass
        year = list_nomb[2].strip()
        list_year = year.split(".")
        year = list_year[0]
        return True, dia, mes, year

    except Exception as e:
        print ("""\nEl nombre de este archivo no es el correcto. Debe corresponder a la fecha del registro.
               Recuerda que el formato es'dd-mm-aaaa.csv'""")
        return False, "", "", ""


#validación del archivo .csv con los registros:
#INFORMACIÓN IMPORTANTE: El nombre del archivo debe tener el siguiente formato "dia-mes-año.csv"
def verificar_archivo_csv (ruta, reg):
    try:
        lista_sin_format = []
        lista_con_format = []
        dicc_reg = {}
        observacion = open(ruta, "r")
        for i in observacion:
            lista_sin_format.append(i.split(";"))
        

        for j in lista_sin_format[1:]:
            cod = j[0].strip()
            nombre_obs = j[1].strip()
            t_max = float(j[2].strip())
            t_min = float(j[3].strip())
            dicc_reg[cod] = {"nombre": nombre_obs,"fecha": {"dia": nombre_csv(reg)[1], "mes" : nombre_csv(reg)[2], "año": nombre_csv(reg)[3]},"temp_max" : t_max,"temp_min" : t_min}
            lista_con_format.append(dicc_reg)
            dicc_reg = {}
            

        observacion.close
        return lista_con_format

    except Exception as e:
        print (f"\nEl archivo {reg} no corresponde al registro de los observatorios.")
        input ("Presione cualquier tecla para salir")
        

        
    
        



#DESARROLLO DEL PROGRAMA
registro = "02-02-2023.csv" #archivo .csv con los registros de temperatura. Su nombre es la fecha del registro [dia-mes-año]
carpeta = "filtro_1"
ruta = f"{carpeta}/{registro}"
while True:
    print (verificar_archivo_csv (ruta, registro))
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
            
    

            