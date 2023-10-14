
#Esta función verifica que el archivo existe en la carpeta y lo abre si existe
def validar_archivo(carp, msj):
    try:
        nombre_archivo = input(msj)
        archivo = open(f"{carp}/{nombre_archivo}", "r")
        print("\n", "-" * 20)
        print ("| ARCHIVO EXISTENTE |")
        print("-" * 20)
        return True, archivo
    except Exception as e:
        print ("\n", "*" * 40)
        print ("ERROR!!\nLo sentimos, este archvio no existe")
        print ("*" * 40)
        return False, ""

def prom (sum, n):
    return sum/n

#DESARROLLO DEL PROGRAMA
carpeta = "Archivos" #Carpeta donde se encuentra contenido el archivo

print (":" * 46)
print (":  PROMEDIO DE SPAM DEL SERVIDOR DE CORREOS  :")
print (":" * 46)
validar_arch = validar_archivo(carpeta, "\nINGRESAR NOMBRE DEL ARCHIVO: ")
archivo = validar_arch[1]

#input ("\npresione cualquier tecla para continuar... ")
if validar_arch[0] == True: #Verifica si encuentra el archivo. Si lo encuentra empiezo a intentar calcula el promedio de spam
    cl = 0 #Contador de línea
    suma_spam = 0
    for linea in archivo:
        if linea.startswith("X-DSPAM-Confidence:"):
            spam_str = linea.split()[1]
            spam_str = spam_str.strip() #quita los espacios vacios
            suma_spam += float(spam_str) #el elemento lo agarra como cadena y lo cobvierte en float para poder sumar
            
            cl += 1
    archivo.close()

    if cl > 0: #Verifica si el archivo corresponde a servidor de correos. Si es así, imprime el promedio de SPAM
        print ("\n", "-*" * 20)
        print (f"Promedio de confianza de SPAM: {prom(suma_spam, cl):.4f}")
        print ("-*" * 20)
        input("\npresione cualquier tecla para finalizar... ")
    else:
        print ("AVISO: Este archivo no corresponde al servidor de correos.")
else:
    input("presione cualquier tecla para finalizar... ")




