"""Este programa está diseñado como servicio de la empresa ACME para calcular el valor de la nómina de un empleado,
el sueldo bruto y el sueldo neto del mismo.
"""

#El sueldo bruto se calcula a partir de las horas y el valor de la hora.

valor_hora = 20000 #Valor de la hora

horas_trabajadas = int(input("cantidad de horas trabajadas por el empleado: ")) #Cantidad de horas trabajadas por el empleado
sueldo_bruto = valor_hora * horas_trabajadas #sueldo bruto del empleado

#Al sueldo bruto se le descuenta el valor de la EPS  (4% del sueldo bruto) y el valor de pensión (4% del sueldo bruto).

porc_eps = 0.04 #Valor decimal equivalente al descuento del valor de la EPS (4%)
porc_pension = 0.04 #Valor decimal equivalente al descuento del valor de la pensión (4%)

descuentos = (porc_eps + porc_pension) * sueldo_bruto #Valor equivalente a los descuentos del sueldo bruto

#El sueldo neto se halla restando el sueldo bruto menos los descuentos
sueldo_neto = sueldo_bruto - descuentos #sueldo neto del empleado

print ("Sueldo bruto = ", f"${sueldo_bruto:,}")
print ("\nDescuento EPS = ", f"${porc_eps * sueldo_bruto:,}")
print ("\nDescuento pensión = ", f"${porc_pension * sueldo_bruto:,}")
print ("\nTotal descuentos = ", f"${descuentos:,}")
print ("\nSueldo neto = ", f"${sueldo_neto:,}")



