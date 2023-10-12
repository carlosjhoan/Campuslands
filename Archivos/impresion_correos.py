#Programa que imprime los correos en consola




archivo = open("Archivos/mbox-short.txt", "r")
archivo_msj = open("Archivos/mensajes.txt", "w")
cl = 0
#set_email =
for linea in archivo:
    if linea.startswith("Subject:"):
        #cl += 1
        #email = linea.split()[1]
        #print (email)
        archivo_msj.write(linea.split(":")[2])



archivo.close()
archivo_msj.close()
#cl = len(set_email)
lista_alf = []

print(f"Cantidad de correos de origen distinto: {cl}")
#for email in set_email:
    #lista_alf.append(email)
    #lista_alf.sorted()
    #print (email)

#for i in sorted(lista_alf, reverse = False, key = lambda x:len(x)): #imprime los correos de menor cantidad a mayor
    #print (f"{i} enviado [ok]")