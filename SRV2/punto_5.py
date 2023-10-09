"Con este algoritmo se le permite a un usuario obtener obtener su calificación ajustada a la curva del 8"

#Calificación entre 0.0 y 5.0 a ajustar según el ususario
calif = float(input("Ingrese su calificación: "))

#Una vez ingresado el valor de la calificación se debe hallar el valor ajustado a la curva del 8
calif_curv_8 = (calif * 0.8) + 1

print ("Su calificación ajustada a la curva del 8 es: ", calif_curv_8)