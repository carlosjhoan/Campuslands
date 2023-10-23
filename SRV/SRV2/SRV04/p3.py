"Este programa genera *1.000.000* de puntos dentro del rectángulo de la simulación de montecarlo."

import random
import math

cant_num = 1000000

number_of_hits =0

for i in range(cant_num):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x**2 + y**2) <=1:
        number_of_hits +=1
    #print ("x = ", x, "\ny =", y)

pi = 4 * number_of_hits / cant_num

print ("Number of Hits = ", number_of_hits)
print (f"pi es aprox = {pi:.2f}", )