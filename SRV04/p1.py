"Este programa determina si un número es perfecto o no."


num = int(input("Ingrese el número a verificar: "))

suma = 0


print ("Divisores")

#Se aplica un for para que itere en un rango de número que empiece en 1 hasta 1 menos que el número de entrada con paso 1.
for i in range(1, num, 1):

    if num % i == 0:
        print (i)
        suma += i

if suma == num:

    print ("\n", num, "Es un número PERFECTO!!")

else:
    print ("\n", num, "NO es un número perfecto.")

