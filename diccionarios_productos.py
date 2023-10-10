def ord_burbuja (lst):
    N = len(lst)
    for i in range (0, N - 1):
        for j in range (i + 1, N):
            if lst[i][1]["precio"] > lst[j][1]["precio"]: #si fuera de mayor a menor se reemplaza por <
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    return lst

productos = {
    1 : {
        "nombre": "pantalon",
        "precio" : 125,
        "cantidad" : 5
    },
    2 : {
        "nombre": "camisa",
        "precio" : 200,
        "cantidad" : 25
    },

    3 : {
        "nombre": "zapatos",
        "precio" : 50,
        "cantidad" : 25
    }

}

list_productos = list(productos.items())
lst_ord = ord_burbuja (list_productos)
print (lst_ord) #Imprime la loista ordenada
productos = dict(lst_ord)
print (productos)