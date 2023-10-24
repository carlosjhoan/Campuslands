#Para ir probando pedazos de código
archivo = open("filtro_1/03-02-23.csv", "r")
lista_vac = []
contenido = archivo
for i in contenido:
    lista_vac.append(i.split(";"))
    

archivo.close()
print (lista_vac[1:])

