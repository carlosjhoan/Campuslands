import time

tiempo_incial =time.time()
letra = input("ingrese letra")
tiempo_final = time.time()
print (f"Tiempor transcurrido: {(tiempo_final-tiempo_incial):.2f}")