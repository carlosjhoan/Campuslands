#Función que crea matrices

def crear_matrices_ceros (fil, col):
    m = []
    for i in fil:
        fila = [0] * col
        m.append(fila)
    return m
#Función que imprime matrices
def print_matrices (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print (mat[f][c], end = " "])
        print (" ")

matriz = crear_matrices_ceros(4, 5)

print_matrices(matriz)