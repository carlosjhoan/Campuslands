#Programa que muestra los correos con origen distinto




archivo = open("Archivos/mbox-short.txt", "r")

cl = 0
set_email =set()
for linea in archivo:
    if linea.startswith("From:"):
        #cl += 1
        #email = linea.split()[1]
        #print (email)
        set_email.add(linea.split()[1])


archivo.close()
#archivo_msj.close()
cl = len(set_email)
lista_alf = []

print(f"Cantidad de correos de origen distinto: {cl}")
for email in set_email:
    lista_alf.append(email)
    #lista_alf.sorted()
    #print (email)

for i in sorted(lista_alf, reverse = False, key = lambda x:len(x)): #imprime los correos de menor cantidad a mayor
    print (i)
    #Imprime correo