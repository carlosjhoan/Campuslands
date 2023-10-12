fd = open ("Archivos/nombres.txt", "r")
fd_2 = open ("Archivos/nombres_2.txt", "w")

for linea in fd:
    fd_2.write(linea)
#fd.read()

fd.close()
fd_2.close()

print ("Proceso Terminado")