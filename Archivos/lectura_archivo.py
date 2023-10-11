archivo = open("Archivos/nombres.txt", "r")


texto = archivo.read()
print ("\ntexto:\n",texto) #Me ubica el descriptor al final

archivo.seek(0) #Se ubica en la posición 0
texto_2 = archivo.readline() #Es la que más se utiliza para no correr el riesgo sin quedarnos sin memoria
print ("\ntexto_2:\n",texto_2)

texto_3 = archivo.readlines()
print ("\ntexto3:\n",texto_3)

archivo.close()