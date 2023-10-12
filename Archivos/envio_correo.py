#Programa que muestra los correos con origen distinto




fd = open("Archivos/mbox-short.txt", "r")
archivo_msj = open("Archivos/mensajes.txt", "w")
cl = 0
set_email =set()
for linea in fd:
    if linea.startswith("To:"):
        #cl += 1
        #email = linea.split()[1]
        #print (email)
        set_email.add(linea.split()[1])



fd.close()

cl = len(set_email)
lista_alf = []

print(f"Cantidad de correos de origen distinto: {cl}")
for email in set_email:
    lista_alf.append(email)
    #lista_alf.sorted()
    #print (email)

for i in sorted(lista_alf, reverse = False, key = lambda x:len(x)): #imprime los correos de menor cantidad a mayor
    print (f"{i} enviado [ok]")
    archivo_msj.write(f"{i} enviado [ok]\n")

archivo_msj.close()

