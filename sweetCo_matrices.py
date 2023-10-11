#Este programa recibe la matriz de ventas semanales de la empresa SweetCo

def cal_prod_max_ing_semana(mat_vtas, mat_prc):
    fil = len(mat_vtas)
    lst_tot_vtas = [0] * fil

    for  f in range (fil):
        lst_tot_vtas[f] =sum(mat_vtas[f] * mat_prc[f])

    max_vtas = max(lst_tot_vtas)
    prdo_max_vtas = lst_tot_vtas.index(max_vtas) + 1
    return prdo_max_vtas





def ventas_dia(mat, mt_prc):
    ventas_dias = []
    vta_dia = []

    for c in range(len(mat[0])):
        for f in range(len(mat)):
            vta_dia.append(mat[f][c] * mt_prc[f])
        ventas_dias.append(sum(vta_dia))
        vta_dia = []
    print (ventas_dia)
    return ventas_dias  

def dia_mayor_venta (vtas_dias, dias_sem):
    print (len(vtas_dias))
    print (len(dias_sem))
    for i in range(len(vtas_dias)):
        if vtas_dias[i] == max(vtas_dias):
            
            return dias_sem[i], max(vtas_dias)

        




mat_ventas = [[100, 88, 92, 94, 85, 110, 118],
              [30, 42, 31, 32, 38, 40, 37],
              [23, 35, 39, 45, 55, 60, 61],
              [45, 50, 56, 65, 47, 57, 68],
              [18, 25, 33, 21, 22, 28, 32]]

mat_precios = [1500, 5000, 6500, 2500, 22500]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
prd_max_ing_sem = cal_prod_max_ing_semana(mat_ventas, mat_precios)
ventas_cada_dia =  ventas_dia(mat_ventas, mat_precios) 
dia_max_venta = dia_mayor_venta(ventas_cada_dia, dias_semana)
print (f"El producto que más vende es: {prd_max_ing_sem}")
print (f"El día de la semana con mayor venta es el: {dia_max_venta[0]}\nVentas del día: ${dia_max_venta[1]:,} ")
#print (f"Ventas de cada día: {prd_max_ing_sem[1]}")

#print ([0] * 4)