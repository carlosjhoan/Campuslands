"Este programa nos indica en cuántos años se duplicará el costo de la matrícula de una universidad."

import random


cost_matr_0 = 10000

porc_int_an = 0.07 #Interés anual equivalente al 7%



for i in range (1, 12):

    cost_matr =  1.07**i * cost_matr_0 #Valor de la matrícula apenas pasado cada año

    if cost_matr >= 2 * cost_matr_0:
        print (f"La matrícula se duplica al año {i} y tiene un costo de {cost_matr:,.2f}")
