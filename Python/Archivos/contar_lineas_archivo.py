archivo = open ("Archivos/mbox-short.txt", "r")

n = 0
#for linea in archivo:
 #   n +=1

cp = 0 #catidad palabras

for linea in archivo:
    linea.strip()

    #for i in range(len(linea)):
        #if i
    #cp += len(linea.split(" "))
    for lin in linea.split(" "):
        if lin.isalnum():
            cp += 1

archivo.close()
print (f"Cantidad de palabras: {cp}")