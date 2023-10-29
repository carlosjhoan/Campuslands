#Función que crea matrices

def crear_matrices_ceros (fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

#Función que imprime matrices
def print_matrices (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print (mat[f][c], end = " ")
        print (" ")

def llenar_matriz (mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat [f][c] = int(input (f"Valor de la posición [{f+1}][{c+1}]: "))
        print (" ")   

matriz = crear_matrices_ceros(4, 5)
llenar_matriz (matriz)

print_matrices(matriz)