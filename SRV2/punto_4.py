"""Este programa debe ser capaz de calcular y posteriormente imprimir en pantalla 
la cantidad de horas, minutos y segundos restantes dada una cantidad de segundos. """ 

#Cantidad de segundos establecidos según el ususario
segundos = int(input("Cantidad de segundos a convertir: "))
               
#Primero se establecen la constantes referentes a la cantidad de segundo que hay en una hora y en un minuto respectivamente
seg_en_hora = 3600 #Cantidad de segundos en una hora
seg_en_min = 60 #Cantidad de segundos en un minuto

#Acto seguido se calcula la cantidad de horas exactas que hay en la cantidad de segundos dados. Para ello hacemos tomamos el valor del cociente de dividir los segundos en horas. Esto se hace con la divisón entera.
cant_horas = segundos // seg_en_hora

#A continuación, se hallan los minutos. Estos minutos se calculan teniendo como referencia los segundos restantes una vez hallada la cantidad de horas.
#La cantidad de segundos restantes una vez halladas las horas se deben dividir (divisón entera) entre la cantidad de segundos en un minuto (60) y el resultando sería la cantidad de minutos
cant_min = (segundos - (cant_horas * seg_en_hora)) // seg_en_min

#Por último se calcula la cantidad de segundos restantes. Para esto se deben restar de los segundos establecidos, los segundos según las horas halladas ylos segundos según los minutos halladas, lo cual nos dará el resultado de los segundos restantes.
cant_seg = segundos - (cant_horas * seg_en_hora) - (cant_min * seg_en_min)


print ("Horas = ", cant_horas)
print ("Minutos = ", cant_min)
print ("Segundos = ", cant_seg)






