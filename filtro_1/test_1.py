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


#FUNCIONES DE LISTAR 

#Esta función lista los observatorios por código
def listar_cod_1 (lst_registros):
    list_cod = []
    list_cod_nomb = []
    list_cod_1 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_cod.append(int(cod_i))
            
    set_cod = set(list_cod)
    list_cod = sorted(list(set_cod))
    
        
    for j in list_cod:
        list_cod_nomb.append(str(j))
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if str(j) == cod_k:
                nom_obs = k[str(j)]["nombre"]
        list_cod_nomb.append(nom_obs)
        list_cod_1.append(list_cod_nomb)
        list_cod_nomb = []
    
    return list_cod_1

#Esta función lista los observatorios por código
def listar_cod_2 (lst_registros):
    list_nomb = []
    list_nomb_cod = []
    list_cod_2 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_nomb.append(i[cod_i]["nombre"])
            
    set_nomb = set(list_nomb)
    list_nomb = sorted(list(set_nomb))
     
    for j in list_nomb:
        list_nomb_cod.append(j)
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if j == k[cod_k]["nombre"]:
                cod_list = cod_k
        list_nomb_cod.append(cod_list)
        list_cod_2.append(list_nomb_cod)
        list_nomb_cod = []
    
    return list_cod_2

##Esta función lista las observaciones a nivel por código y con paginación de 10
def listar_cod_5 (lst_registros):
    list_cod = []
    
    list_cod_5 = []
       
    for i in lst_registros:
        cod_i = list(i.keys())[0]
        list_cod.append(int(cod_i))
            
    set_cod = set(list_cod)
    list_cod = sorted(list(set_cod))
    
        
    for j in list_cod:
        
        for k in lst_registros:
            cod_k = list(k.keys())[0]
            if str(j) == cod_k:
                list_cod_5.append(k)
        
    return list_cod_5

#Función que me permite verificar si el archivo .json existe. SI no existe lo crea
def verificar_archivo (ruta):
    try:
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros

    except:
        
        archivo = open(ruta, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta, "r")
        lista_libros = json.load(archivo)
        archivo.close
        return lista_libros


#validación del archivo .csv con los registros:
#INFORMACIÓN IMPORTANTE:La fecha en el archivo .csv está en formato "dd-mm-aaa"
def verificar_registro_csv (ruta_csv):
    try:
        lista_sin_format = []
        lista_con_format = []
        dicc_reg = {}
        observacion = open(ruta_csv, "r")
        for i in observacion:
            lista_sin_format.append(i.split(";"))
        print ("lista sin format", lista_sin_format)
        

        for j in lista_sin_format[1:]:
            cod = j[0].strip()
            nombre_obs = j[1].strip()
            t_max = float(j[2].strip())
            t_min = float(j[3].strip())
            fecha = j[4].strip()
            fecha = fecha.split("/")
            dia = fecha[0]
            mes = fecha[1]
            year = fecha[2]


            dicc_reg[cod] = {"nombre": nombre_obs,"fecha": {"dia": dia, "mes" : mes, "año": year},"temp_max" : t_max,"temp_min" : t_min}
            lista_con_format.append(dicc_reg)
            dicc_reg = {}

        print (lista_con_format)    
        observacion.close
        return lista_con_format

    except Exception as e:
        print (f"\nEl archivo no corresponde al registro de los observatorios.")
        input ("Presione cualquier tecla para salir")
        

#Función que me permite verificar si el archivo .json existe. SI no existe lo crea
def verificar_archivo_json (ruta_json):
    try:
        archivo = open(ruta_json, "r")
        lista_registros_obs = json.load(archivo)
        archivo.close
        return lista_registros_obs

    except:
        
        archivo = open(ruta_json, "w")
        json.dump([], archivo)
        archivo.close()
        archivo = open(ruta_json, "r")
        lista_registros_obs = json.load(archivo)
        archivo.close
        return lista_registros_obs

#Esta función registra la información actualizada al json 
def cargar_libro (lsta_registros, ruta_json):


        archivo = open(ruta_json, "w")
        json.dump(lsta_registros, archivo)
        archivo.close()
    
#Esta función me permite añadir los datos del registro csv al json. Me devulve la lista de información completa.
def csv_json (lst_csv, lst_json):
    for i in lst_csv:
        lst_json.append(i)

    return lst_json
   
    
        



#DESARROLLO DEL PROGRAMA
 #archivo .csv con los registros diarios de temperatura. Su nombre es la fecha del registro [dia-mes-año]
archivo_json = "obervatorios.json" #Este es el nombre del archivo .json que contiene la información de todos los observatorios. Recogida diariamente
carpeta = "filtro_1"

#RUTAS: json y csv
ruta_csv = "filtro_1/datos.csv" #Ruta del registro diaro de datos (formato csv)
ruta_json = f"{carpeta}/{archivo_json}" #Ruta del archivo que contiene el historial de los registros(formato json)

#LEER LISTAS y CARGARLAS AL JSON
lista_csv = verificar_registro_csv (ruta_csv)
lista_json = verificar_archivo_json (ruta_json) #Inicializar archivo json
lista_registro_obs = lista_csv #Lista con la información actualizada
cargar_libro (lista_csv, ruta_json)
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
        #print (listar_cod_1 (lista_registro_obs))
        print ("\n      1. LISTADO DE OBSERVACIONES POR CÓDIGO")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 24)
        print("|CÓDIGO\t|   NOMBRE\t|")
        print ( "=" * 25)

        for i in listar_cod_1 (lista_registro_obs):
            if len(i[1]) <= 5:
                i[1] = i[1] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        input("Presiona cualquier tecla para volver al menú... ")
                  
                  

    elif opc == 2:
        #print (listar_cod_2 (lista_registro_obs))
        print ("\n      2. LISTADO DE OBSERVACIONES POR NOMBRE")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 24)
        print("| NOMBRE\t|CODIGO |")
        print ( "=" * 25)

        for i in listar_cod_2 (lista_registro_obs):
            if len(i[0]) <= 5:
                i[0] = i[0] + " "
            print (f"| {i[0]}\t| {i[1]}\t|")
            print ("." * 25)

        input("Presiona cualquier tecla para volver al menú... ")

    elif opc == 3:
        pass

    elif opc == 4:
        pass

    elif opc == 5:
        #print (listar_cod_2 (lista_registro_obs))
        n = 0
        print ("\n      5. LISTADO DE OBSERVACIONES NACIONALES")
        print ("\t", "-" * 40)
        print ("\n\n", "=" * 72)
        print("|CÓDIGO\t|   NOMBRE\t| Temp max [°C]\t| Temp min [°C]\t| Temp prom [°C]|")
        print ( "=" * 73)
        
        for i in listar_cod_5 (lista_registro_obs):
            cod_i = list(i.keys())[0]
            nombre = i[cod_i]["nombre"]
            if len(nombre) <= 5:
                nombre = nombre + "  "
            t_max = i[cod_i]["temp_max"]
            t_min = i[cod_i]["temp_min"]
            t_prom = (t_max + t_min)/2
            print (f"| {cod_i}\t| {nombre}\t|  \t{t_max}\t|  \t{t_min}\t|  \t{t_prom:.2f}\t|")
            print ("." * 73)
            n += 1
            if n == 10:
                n = 0
                input (">>> Seguir [ENTER] --> \n")



    elif opc == 6:
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
            
    

            