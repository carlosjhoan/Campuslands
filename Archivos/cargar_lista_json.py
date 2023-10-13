import json

fd = open("Archivos/lista_1.json", "r")

lst = []

lst = json.load(fd)
print ("-" * 40)
print ("       NOMBRE\t\t|\tEDAD  ")
print ("-" * 40)
for i in lst:
    
    print (f"\t{i['nombre']}   \t|\t{i['edad']}")
    #print (f"EDAD: {i['edad']}")
    print ("-" * 40)

fd.close()