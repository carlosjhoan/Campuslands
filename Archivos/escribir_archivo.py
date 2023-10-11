archivo = open("Archivos/salas.txt", "w")

archivo.write("Sputnik\n\t")
archivo.write("Apolo\n")
archivo.writelines(["Houston\n", "Artemis\n"])
print("\nArchivo: ", archivo)
archivo. close()