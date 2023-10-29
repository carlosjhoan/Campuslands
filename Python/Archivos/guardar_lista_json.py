import json

fd = open("Archivos/lista_1.json", "w")

lst = [{"nombre" : "Paola", "edad" : 25},
       {"nombre" : "Carlos", "edad" : 28},
       {"nombre" : "Juan", "edad" : 18},
       {"nombre" : "Mateo", "edad" : 17},
       {"nombre" : "Patricia", "edad" : 20}]

json.dump(lst, fd)

fd.close()