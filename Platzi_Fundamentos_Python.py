
# coding: utf-8

# # Fundamentos de Python (Platzi)

# In[2]:


print ("Hola, esto es Python")


# In[3]:


print ("Hola, soy Carlos y tengo 27 años")


# Python como calculadora

# In[4]:


print (12+5-7+10)


# In[5]:


print (12)


# In[6]:


print (12+5)


# In[9]:


print (12+5)
print (52)


# # Variables

# In[1]:


my_name = "Carlos"


# In[2]:


print (my_name)


# In[3]:


my_age = 27


# In[4]:


print (my_age)


# In[11]:


my_name = input("Cuál es tu nombre? ")


# In[12]:


print (my_name)


# In[13]:


my_age = input ("Cuántos años tienes? ")


# In[15]:


print ("Ahhh!, tú eres", my_name, "el que tiene", my_age, " años de edad")


# # Concatenación de String

# In[2]:


name = "Carlos"


# In[3]:


last_name = "Aguilar"


# In[6]:


full_name = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
a = "aaabb"
b = "ab"
print (a.split('aa'))


# In[4]:


print (full_name)


# In[5]:


print ("Hola!, mi nombre es {} y mi apellido es {}".format(name, last_name))


# In[9]:


print (f"Hola!, mi nombre es {name} y mi apellido es {last_name}")


# In[2]:


"Si hago la siguiente comparación"
x = 3.3
y = 1.1 + 2.2


# In[3]:


print('x = ', x)
print ('y = ', y)
print ('x == y? ', x == y )


# In[4]:


"Si ahora corto los dígitos de y, para que solo me dé 2 dígitos"
y_str = format(y, ".2g")
print ('y_str = ', y_str)


# In[9]:


y_str


# # LOGIC: AND, OR

# In[12]:


"AND"
print ('True and True = ', True and True )
print ('True and False = ', True and False )
print ('False and True = ', False and True )
print ('False and False = ', False and False )


# In[13]:


"OR"
print ('True or True = ', True or True )
print ('True or False = ', True or False )
print ('False or True = ', False or True )
print ('False or False = ', False or False )


# In[16]:


"Uso del AND"
stock = int(input('Ingrese un número de inventario: '))
print (stock >= 100 and stock <= 1000)


# In[21]:


"Uso del OR"
role = input ("Ingrese su rol: ")
print ("Acceso permitido: ", role == "Admin" or role == "Seller")


# # Condicionales: if, while, etc

# In[1]:


if True:
    print ("Se ejecuta")


# In[3]:


if not False:
    print ("Nunca se ejecuta")


# In[14]:


pet = input ('¿Cuál es tu mascota favorita? => ')
if pet == ('Perro' or 'perro'):
    print ('Excelente!')

if pet == ('gato' or 'Gato'):
    print ('Juuuum, complicado!')

else:
    print ('Ahí no sé qué decir')


# In[20]:


stock = int(input('Digite el nivel de stock:'))
if stock >= 100 and stock <= 1000:
    print ('El stock es permitido')
if stock < 100:
    print ('URGENTE!!! Nivel de stock insuficiente')
if stock > 1000:
    print ('Nivel de stock desbordado')


# # STRING recargado

# In[23]:


text = 'eliana aprendió a programar en Python'
print ('JavaScript' in text) #Busca la palabra JavaScript en text

size =len(text)
print ('El texto tiene', size, 'caracteres.')

print('El texto en mayúscula:', text.upper()) #El texto en Mayúscula
print('El texto en minúscula:', text.lower()) #El texto en minúscula
print ('# de veces que está la letra e: ', text.count('e')) #Cuenta la cantidad de veces que está un caracter en el texto
print (text.swapcase()) #Invierte la mayúsculas por minúsculas y viceversa
print (text.startswith('El')) #Afirma o niega si el texto empieza con las letras que se le indican
print (text.endswith('thon')) #Afirma o niega si el texto Finaliza con las letras que se le indican
print (text.replace('Python', 'JavaScript')) #Reemplaza una palabra por la otra
print (text.capitalize()) #Coloca la primera letra en mayúscula y si hay palabras que empiezan en minuscula, las pasa a Mayúscula
print (text.title()) #Pone todas las palabras iniciando en mayúscula


# # Slicing e Indexing

# In[5]:


text = "Ella sabe programar en Python"
##### INDEXING
print (text[0])
print (text[-1]) #Me bota el último caracter

#### SLICING
print (text[0:7])
print (text[:10])
print (text[3:12:2]) #Aquí indico que quiero ir de la posición 3 a las 11 haciendo saltos de 2 caracteres


# # Listas

# In[3]:


#CRUD: Create, Read, Update, Delete

"Create"
numbers = [1,  2, 3, 4, 5]

"Read"
print ("numbers[1] :", numbers[1])
print ("numbers[0:3]:", numbers[0:3])


"Update"
numbers[-1] = 10
print ("numbers: ", numbers)

#.append() --> para agregar valores al final de la lista
numbers.append(15)
print ("numbers:", numbers)

#.insert() --> me agrega valores a cualquier posición deseada de la lista
numbers.insert(1, 'holi' )
print ("numbers:", numbers)

#Puedo también fusionar listas
tasks = ['Todo 1', 'Todo 2', 'Todo 3']
new_list = numbers + tasks
print ("new_list =", new_list)

#Si quisiera saber el índice de un elemento dentro de la lista
print ("índice de Todo 1:",new_list.index('Todo 1'))

"Delete"
new_list.remove(2) #Remueve el elemento que se le indica
print ("new_list:", new_list)

new_list.pop() #Remueve el último elemento de la lista si no le indico nada
print ("new_list:", new_list)

new_list.pop(2) #Me borra de la lista el elemento con índice 2
print ("new_list:", new_list)

new_list.reverse() #Me voltea el orden de todos los elementos de la lista
print ("new_list:", new_list)

numbers_a = [6, 4, 1, 8, 3, 0, 2, 5, 7]
numbers_a.sort() #Me orden una lista denúmeros de menor a mayor
print("numbers_a.sort:", numbers_a)

strings = ['alberto', 'carlos', 'javier', 'alfonso']
strings.sort() #Me ordena lalistapor orden alfabético
print ("strings.sort():", strings)


# # Tuplas

# In[12]:


numbers = (0, 1, 2, 3, 4, 5)
strings = ('Nicol', 'Andrea', 'Edinson', 'Patricio', 'Eva', 'Andrea')

print ('numbers', numbers)
print('strings:', strings)

#índice de las tuplas
print ('numbers[0]:', numbers[0])
print ('string[0]:', strings[0])

#Algunos métodos de las tuplas

"Índice de un elemento"
print ('índice_Edinson:', strings.index('Edinson'))

"Cantidad de veces que aparece un elemento dentro de la tupla"
print ('Cuenta_Andrea:', strings.count('Andrea'))

"Convertir una Tupla en Lista"
my_list = list(strings)
print ('my_list:', my_list)
print (type(my_list))

my_list[2] = 'Fabiani'
print ('my_list:', my_list) #Modificación de la lista.

"Convertir de lista a tupla"
my_tuple = tuple(my_list)
print ('my_tuple:', my_tuple)


# NOTA: Las Tuplas son tipo de datos de solo lectura, por tanto, no se pueden modificar

# # Diccionarios

# In[10]:


my_dict = {
    'name': 'Carlos',
    'apellido' : 'Aguilar',
    'edad' : 28,
    'nacimiento' : '15-Feb-2023',
    'genero' : 'masculino',
    'ciudad' : 'Floridablanca'
}

print (my_dict['name'])
print ('Len_my_dict:', len(my_dict))
print ('Fecha_nacimiento:', my_dict.get('nacimiento')) #Otra forma de obtener un valor
print ('apellido' in my_dict) #Una forma de saber si una clave está en el diccionario
print ('nnn' in my_dict)


# In[11]:


"Actualizaciones e inserciones en los Diccionarios"

person = {
    'name' : 'Carlos',
    'last_name' : 'Aguilar',
    'langs' : ['Python', 'SQL'],
    'age' : 38
}


person['name'] = 'Fionaro'
person['age'] -= 10    # Puedo modiciar los valores numéricos con operacion aritméticas
person['langs'].append('JavaScript')    # Si dentro del diccionario tengo listas, puedo agregar
#del person['last_name']    # Para eliminar un par clave-valor del diccionario
person.pop('last_name')   # Otra forma de eliminar pares

print ('person :', person)

"items"
print ('items', person.items()) # Me muestra en una tupla los pares clave-valor que hay en el diccionario

"keys"
print ('keys', person.keys()) # Me muestra las claves que contiene el diccionario

"values"
print ('values', list(person.values()) )# Me muestra los valores del diccionario


# # Ciclos

# ### While

# In[10]:


counter_1 = 0
print ("counter_1")
while counter_1 < 10:
    counter_1 += 1
    print ( counter_1)

    
counter_2 = 0
print ("counter_2")
while counter_2 < 20:
    counter_2 += 1
    if counter_2 == 15:
        break
    print (counter_2)
    
counter_3 = 0
print ("counter_3")
while counter_3 < 20:
    counter_3 += 1
    if counter_3 < 15:
        continue
    print (counter_3)


# ### For

# In[5]:


print ("range(20)")
for element in range(20):
    print (element)
    
print ("range(1, 20)")
for element in range(1, 20):
    print (element)

print ("Iterando sobre un diccionario")
my_dict = {
    'name' : 'Carlos',
    'last_name' : 'Aguilar',
    'edad' : 28,
    'sexo' : 'masculino'
}
print ("Ierando las keys")
for element in my_dict:
    print (element)

print ("Iterando los values")
for element in my_dict:
    print (my_dict[element])
    
print ("clave-valor directamente")
for key, value in my_dict.items():
    print (key, ":", value)
    
"Utilizar FOR cuando tenemos una lista de diccionarios"
people = [
    {
        'name' : 'Douglas',
        'last_name' : 'Tristancho',
        'edad' : 27
    },

    {
        'name' : 'Adrián',
        'last_name' : 'Merchán',
        'edad' : 29
    },
    
    {
        'name' : 'Fabiola',
        'last_name' : 'Contreras',
        'edad' : 25
    }
]

for person in people:
    print ("name :", person['name'])


# ### Ciclos anidados

# In[2]:


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for element in matriz:
    for i in element:
        print (i)


# # El Zen de Python

# In[1]:


import this


# ### Conjuntos

# ##### Características
# - Se pueden modificar
# - No tienen un orden
# - No permite duplicados

# In[13]:


set_countries = {'bol', 'col', 'mex', 'col'}
print ('set_countries:',set_countries)
print ('Type(set_countries):', type(set_countries))

set_numbers = {1, 3, 7, 2, 2, 3, 8, 1}
print ('set_numbers:', set_numbers)

set_types = {'Holita', True, 14.381, False, 'Carlos'}
print ('set_types:', set_types) #Puedo tener conjuntos de tipos de datos diferentes

set_string = set('Carlos Jhoan Aguilar Galvis')
print ('set_string:', set_string)

set_tuples = set(('ahj','hjhg', 'ahj', 'vh', 'ugvc'))
print ('set_tuples:', set_tuples)

numbers = [1, 2, 2, 3, 3, 5, 4, 1]
set_numbers_list = set(numbers)

list_numbers = list(set_numbers_list) #Me convierte en lista, el conjunto de números únicos de la lista numbers
print ("numbers:", numbers)
print ('list_numbers:', list_numbers)


# ### NOTA:
# Si agrego un valor repetido en un conjunto, Python solo deja uno de los 2 valores

# ### Modificando conjuntos

# In[10]:


"Saber el tamaño de un conjunto"
set_countries = {'bol', 'col', 'mex', 'col'}
size_set = len(set_countries)
print ("size_set =", size_set)
print ("col in set_countries :", 'col' in set_countries)
print ("pe in set_countries :", 'pe' in set_countries)

"Añadir un elemento al conjunto"
set_countries.add('pe')
print ("set_countries =", set_countries)

"Actualizar un conjunto: Se le puede ingresar una lista de elementos para que sean añadidos al conjunto"
set_countries.update({'ar', 'cub', 'chi', 'bra'})
print ("set_countries =", set_countries)

"Remover un elemento del conjunto"
set_countries.remove('bra')
print ("set_countries =", set_countries)
set_countries.discard ('per') #Si no se encuentra el elemento dentro del conjunto igualmente el programam seguirá su ejecución
print ("set_countries =", set_countries)

"Limpiar todo el conjunto"
set_countries.clear()
print ("set_countries =", set_countries)


# ### Operaciones entre conjuntos

# In[8]:


conj_1 = {'col', 'pe', 'mex'}
conj_2 = {'pe', 'bra', 'arg'}

"unión entre conjuntos"
conj_3 = conj_1.union(conj_2)
print ('conj_3 =', conj_3)
print ('conj_3 =', conj_1 | conj_2) #Otra forma de indicar la unión entre conjuntos

"intersección entre conjuntos"
conj_4 = conj_1.intersection(conj_2)
print ('conj_4 =', conj_4)
print ('conj_4 =', conj_1 & conj_2) #Otra forma de hacer la intersección

"Diferencia"
conj_5 = conj_1.difference(conj_2)
print ('conj_5 =', conj_5)
print ('conj_5 =', conj_1 - conj_2) #Otra forma de hacer la diferencia

conj_6 = conj_2.difference(conj_1)
print ('conj_6 =', conj_6)
print ('conj_6 =', conj_2 - conj_1)

""" Diferencia simétrica """
conj_7 = conj_1.symmetric_difference(conj_2)
print ('conj_7 =', conj_7)
print ('conj_7 =', conj_1 ^ conj_2)


# ### List Comprehension

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# In[7]:


"Forma tradicional de crear una lista con los números del1 al 10"

numbers = []
for element in range (1, 11):
    numbers.append(element)

print ('Numbers :', numbers)

"Forma sencilla aplicando List Comprehension"
numbers_list_comp = [element for element in range(1, 11)]
print ('numbers_list_comp :', numbers_list_comp)

numbers_list_2 = [element * 2 for element in range(1, 11)]
print ('numbers_list_2 =', numbers_list_2)

"Con condicionales"
numbers_list_3 = [i * 2 for i in range (0, 103) if i % 2 == 0]
print ('numbers_list_3 =', numbers_list_3)


# ### Dictionary Comprehension

# ![image.png](attachment:image.png)

# In[7]:


"Forma ordinaria de llenar y crear un diccionario"
dict = {}
for i in range (1, 7):
    dict[i] = i*2 - 1
print ('dict =', dict)

"Dictionary Comprehension"
dict_2 = {i: i*2 - 1 for i in range (1, 7)}
print ('dict_2 =', dict_2)

"De una lista a un diccionario: Forma ordinaria"
import random
countries = ['col', 'per', 'mex', 'bol']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
    
print ("population :", population)

"De una lista a un diccionario: Dictionary Comprehension"
population_2 = {country : random.randint(1, 100) for country in countries}

print ("population_2 :", population_2)

"Otro ejemplo, esta vez utiliando 2 listas"
names = ['Carlos', 'Bochini', 'Destro']
ages = ['28', '45', '32']

dict_new ={name : age for (name, age) in zip(names, ages)}
print ('dict_new :', dict_new)

"Otra solución al ejemplo es:"
new_dict_2 = {names[i] : ages[i] for i in range(len(names))}
print ('new_dict_2 :', new_dict_2)




# ### Funciones

# ![image.png](attachment:image.png)

# In[13]:


"Ejemplo 1"
def my_print (cont):
    print (cont)
    
my_print('Hola')

"Ejemplo 2"
def suma_print (a, b):
    print (a + b)

suma_print(1, -3)
suma_print(5, 7)

"Uso del return"
def sum_range(a, b):
    sum = 0
    for x in range (a, b):
        sum += x
    return sum

sum_range (10,20)

"Ejemplo para hallar el volumen de una caja"
def vol_box(l, w, h):
    return l * w * h
print ('vol_box =', vol_box(1, 3, 5))

"Función con argumentos predeterminados"
def vol_box_2(l = 1, w = 1, h = 1):
    return l * w * h

print ('vol_box_2 =', vol_box_2())

#Si tengo los argumentos predeterminados, pero quiero colocar un valor a un argumento
V = vol_box_2(h = 15)
print(V)

"Si queremos tener varios return, el resultado final es una tupla y lo podemos hacer así ..."
def vol_box_3(l = 1, w = 1, h = 1):
    return l * w * h, l, w, h, 'listo!'  #Es decir, cada return va separado por coma (,)
V = vol_box_3(4, 5, 3)
print (V[0])


# ### NOTA
# Cuando tenemos un multi-return, debemos tener en cuenta que el resultado de la función es una tupla, por tanto, se trata como tal. 

# ### Scope

# In[4]:


price = 100 #Este price se define como variable global

def scope():
    a = price + 100
    print (a)

scope()


# ![image.png](attachment:image.png)

# ### Funciones lambda
# 
# Sintaxis: 
# lambda args : return_value

# In[3]:


"La manera tradicional de crear funciones"
def increment(x):
    return (x + 1)

"Con funciones lambda"
increment_2 = lambda x : x + 1

print("increment (x = 23) :", increment(23))
print ("increment_2 (x = 23) :", increment_2(23))

full_name = lambda name, last_name : f'My full name is {name.title()} {last_name.title()}'
print (full_name('carlos jhoan','aguilar galvis'))


# ### HOF : High Order Functions
# 
# COnsiste en ejecutar funciones dentro de otras funciones. Para ello, hay una funci´n de orden superior que recibe como argumento otra función.

# In[6]:


"Funciones HOF de la forma tradicional"
def incr (x):
    return x + 1

def hof (x, func):
    return x + func(x)

print ('incre(10) =', incr(10))
print ('hof(10, incr) =', hof(10, incr))

"Funciones HOF con lambdas"
incr_lambda = lambda x : x + 1

hof_lambda = lambda x, func : x + func(x)

print ('incre(10)_lambda =', incr_lambda(10))
print ('hof_lambda(10, incr_lambda) =', hof(10, incr_lambda))


# ### Map
# 
# Su función principal es hacer transformaciones a una lista dada de elementos. Esto se hace aplicando una función a la lista.
# 
# ###### NOTA
# Si se mapean 2 o más listas de diferente tamaño, el resultado tendrá la cantidad de elementos de la lista de menor tamaño.

# In[8]:


numbers = [0, 3, 5, 7, 9]
numbers_v2 = map(lambda i : i - 1, numbers)

print ('numbers =', numbers)
print ('numbers_v2 =', list(numbers_v2))
print ('type_map :', type(numbers_v2))

"También puedo aplicar un map a 2 listas o más"
num_1 = [1, 2, 3, 4, 5, 6]
num_2 = [0, 12, -2, 7]
num_3 = [20, 9, -3, -5, 10]

num_total = map (lambda x, y, z : 2*x - y + 3*z, num_1, num_2, num_3)
print ('num_1 =', num_1)
print ('num_2 =', num_2)
print ('num_3 =', num_3)
print ('num_total =', list(num_total))


# ### Map con diccionarios

# In[4]:


items = [
    {
        'product' : 'camisa',
        'price' : 100
    },
    
    {
        'product' : 'pantalón',
        'price' : 200
    },
    
    {
        'product' : 'zapatos',
        'price' : 300
    }
    
    
]

prices = list(map(lambda item: item['price'], items))
print ('prices =', prices)

#Si quisiera agregar un nuevo parámetro a cada diccionario de la lista, podemos hacerlo de la siguiente forma

def taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(taxes, items))
print ('new_items =', new_items)

print ('items =', items) #Se puede ver que SÍ modifica el array original


# Uno de los problemas con MAP es que puede llegar a modificar el array original. Esto ocurre porque con MAP se modifica la referencia de memoria del array, por lo que hay que garantizar que la modificación se haga creando un nuevo elemento, sin modificar el original. Aquí se hacen mención a los término "mutabilidad" e "inmutabilidad".

# In[8]:


items = [
    {
        'product' : 'camisa',
        'price' : 100
    },
    
    {
        'product' : 'pantalón',
        'price' : 200
    },
    
    {
        'product' : 'zapatos',
        'price' : 300
    }
    
    
]

def taxes(item):
    new_list = item.copy()
    new_list['taxes'] = new_list['price'] * 0.19
    return new_list

new_list = list(map(taxes, items))
print ('new_list =', new_list)

print ('old_list =', items) #Se puede ver que SÍ modifica el array original


# ### Filter

# In[3]:


numbers = [1, 2, 3, 4, 5]
new_numbers = filter(lambda x : x % 2 == 0, numbers)
print ('new_numbers', list(new_numbers))

"Ejemplo con lista de diccionario"
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

new_matches = list(filter(lambda item : item['home_team_result'] == 'Win', matches))
print ('matches =', matches)
print ('\nnew_matches =', new_matches)
print (len('hola'))


# ### Reduce

# In[8]:


import functools

numbers = [8, 0, 3, 4]

def accum (counter, item):
    print ('counter ->', counter)
    print ('item ->', item)
    return counter + item
sum = functools.reduce(accum, numbers)
print ('sum_1_10 :', sum)


# ### Módulos

# In[1]:


import sys
print (sys.path)

"Ejemplo del uso del módulo time"
import time
timestamp = time.time()

local = time.localtime()
local_time = time.asctime(local)

print ('timestamp :', timestamp)
print ('local_time :', local_time)


"Ejemplo de uso de collections: contar la frecuencia de números en una lista"
import collections
numbers = [0, 1, 5, 2, 2, 3, 4, 5, 1, 1, 0, 3, 0, 3, 7, 5, 12, 1, 2]
counter = collections.Counter(numbers)
print ('counter :', counter)

import module_1

print (module_1.get_population())
print (module_1.A)
print (module_1.B)

data_countries = [
    
    {
        'Country' : 'Colombia',
        'Population' : 300
    },
    
    {
        'Country' : 'Bolivia',
        'Population' : 200
    },
    
    {
        'Country' : 'México',
        'Population' : 600
    }
]

print ('Pop_Bolivia =', module_1.population_by_country(data_countries, 'Bolivia'))


# In[2]:


import module_1
 


# In[3]:


data_countries = [
    
    {
        'Country' : 'Colombia',
        'Population' : 300
    },
    
    {
        'Country' : 'Bolivia',
        'Population' : 200
    },
    
    {
        'Country' : 'México',
        'Population' : 600
    }
]
print ('Pop_Bolivia =', module_1.population_by_country(data_countries, 'Bolivia'))


# Tenemos un problema cuando tengo un archivo, por ejemplo, __main.py__ que bien puede ser un módulo que se pueda ser usado en otro archivo, pero si lo ejecuto directamente no me hace nada. 
# 
# Puedo revertir esta situación utilizando
# 
# ##### if _ _ name _ _ == '_ _ main _ _':
#         
#         function()
# 
# Esto hace que si yo ejecuto el script directamente, haya algo por ejecutarse. 
# 

# In[2]:


from modules_1.module_2 import function_1, function_2, function_3, function_4
print (function_4())


# ### Iterables 
# #### iter() y next()

# In[5]:


my_range = range(1, 11) #Esto como tal no es un iterable
print ('my_range :', my_range)

my_iter = iter(my_range) #Así queda convertido en un iterable, pero no es una lista
print ('my_iter :', my_iter)

"Si queremos empezar a iterar sobre my_iter, utilizamos next"
print ('1er valor =', next(my_iter)) #imprime el primer valor de range(1, 11)
print ('2do valor =', next(my_iter)) #imprime el segundo valor de range(1, 11)


# ### Manejo de errores
# 
# Podemos darle un manejo a nuestros propios tipos de errores. 
# 
# __raise__ *Exception* (declaration)

# In[3]:


age = 20
if age < 18:
    raise Exception('No se permite el ingreso a menores de edad')
else:
    print (Exception)
    


# __try:__  
#     *action*  
# __except__ *type error*  __as__ *error*  
#     print (/////////)

# In[5]:


try:
    print (0/0)
except ZeroDivisionError as error:
    print (error)
    
print ('NOTA: Pude seguir a pesar del error!!')

try:
    assert 1 != 1#, 'Uno es uno'
except AssertionError as error:
    print (error)

"Mis propios errores"
age = 10
try:
    if age < 18:
        raise Exception('PAILAS!! \n No se permite el ingreso a menores de edad')
except Exception as error:
    print (error)

print ('Todos los errores juntos')
"Puedo juntar varios try-except"
try:
    
    assert 1 != 1, 'Uno es uno'
    print (0/0)
    if age < 18:
        raise Exception('PAILAS!! \n No se permite el ingreso a menores de edad')

except Exception as error:
    print (error)
except AssertionError as error:
    print (error)
except ZeroDivisionError as error:
    print (error)
    

"Uso del else"
try:
    print('Hola')
    
except: 
    print ('Algo anda mal')

else: 
    print ('Todo súper bien')

"Uso del finally"
try:
    print (0/0)
except:
    print ('Esa división no se puede hacer')
finally:
    print ('SIGA y NO PARE BOLAS')
print ('listo!')
    


# ### Reading a .txt file

# In[19]:


#file = open('./t_x_t_1.txt')
"Lee todo el archivo"
#print (file.read())

"Lee el archivo línea a línea. Funciona como un iterador"
#print (file.readline())
#print (file.readline())

"Otra forma de leerlo línea a línea"

#for line in file:
   # print (line)

"cerramos el archivo"
#print (file.close())

"Lo lee y lo cierra al instante"
with open('./t_x_t_1.txt') as file:
    for line in file:
        print (line)

    


# ### Writting on a .txt file
# 
# Por defecto, cuando uno abre un archivo con la sentencia __open('name_file.txtx')__ implícitamente se abre en SOLO MODO LECTURA, es decir, se abre como si la sentencia fuera __open('name_file.txtx', 'r')__.
# 
# Si quisiéramos escribir sobre el archivo, se debe abrir con la sentencia: __open('name_file.txtx', 'w')__. Sin embargo, esta sentencia indica SOLO ESCRITURA, no permite hacer lectura. 
# 
# Si quisiéramos escribir a la vez que leemos el archivo, podemos utilizar la sentencia: __open('name_file.txtx', 'r+')__. Esto lo hace respetando el contenido ya escrito en el archivo. 
# 
# Si quisiéramos sobreescribir el archivo a la vez que podamos leer su contenido, utilizamos la sentencia __open('name_file.txtx', 'w+')__

# In[13]:


with open('./t_x_t_1.txt', 'w+') as file:
    file.write('algo nuevo\n')
    for line in file:
        print (line)
    file.write('algo nuevo\n')


# ### Read a .csv

# In[2]:


import read_csv
import matplotlib.pyplot as plt
import charts

path = './world_population.csv'
data = read_csv.read(path)
country = [row for row in data if row['Country/Territory'] == 'Colombia']
print ('*** Country ***')
print (country[0]['Rank'])

keys_country = list(country[0].keys())
years_pop = []

for year in keys_country:
    if 'Population' in year:
        if year.endswith('ion'):
            years_pop.append(year)
            
years_pop.reverse()

pop = [country[0][year] for year in years_pop] #population of each year

years = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']

'******* Gráfica *******'
charts.g_bar_chart(years, pop)


#for year in years_pop:
#    pop.append(country[0][year])

print ('years :', years)
print ('years_pop :', years_pop)
print ('pop :', pop)

#print ('years_pop :', years_pop)
#print ('leng_years_pop :',len(years_pop))



#print (keys_country)

#years = ['1970', '1980', '1990', '2000', '2010', '2020', '2022']


#print (data[2]['Country/Territory'])


# ### Gráficas con Matplotlib
# 

# In[4]:


import matplotlib.pyplot as plt

def g_bar_chart():
    
    labels = ['a', 'b', 'c']
    values = [1, 5, 10]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
g_bar_chart()


# In[2]:


import charts

keys = ['perros', 'gatos', 'caballos']
quant = [200, 50, 23]
charts.g_bar_chart(keys, quant)


# In[2]:


import charts

keys = ['perros', 'gatos', 'caballos']
quant = [200, 50, 23]
charts.g_pie_chart(keys, quant)


# In[6]:


import read_csv
import matplotlib.pyplot as plt
import charts

path = './world_population.csv'
data = read_csv.read(path)

countries = []
wd_pct = []
for row in data: 
    countries.append(row['Country/Territory'])
    wd_pct.append(row['World Population Percentage'])

charts.g_pie_chart(countries, wd_pct)    
#print ('Countries', countries)
#print ('wd_pct', wd_pct)


# In[1]:


a = {1, 2}
b = {2, 3}
print (a - b)
print (b - a)
l = 1
m = 'hola'


try:
    assert type(m) == type(l), "No es un string"
except AssertionError as error:
    print (error)
    
day = input("Día de nacimiento: ")

a = 0

try:
    type(int(day) - a) == type(a)
except ValueError:
    print ('Debe ser un entero')
    

a = 0
"Fecha de nacimiento"
i = True
while i == True:
    day = input("Día de nacimiento")
    try:
        type(int(day) - a) == type(a)
    except ValueError:
        print ('Debe ser un número')
        i = True
    else:
        i = False


# In[4]:


months: {'e' : 'Enero',
         'f':'febrero',
         'mr' : 'Marzo',
         'ab' : 'Abril',
         'my' : 'Mayo',
         'jn' : 'Junio',
         'jl' : 'Julio',
         'ag' : 'Agosto',
         's' : 'Septiembre',
         'o' : 'Octubre',
         'n' : 'Noviembre',
         'd' : 'Diciembre'
        }
print (months['e'])
a = 'Hola'
print (1+a)


# Punto_1 -- SRV 03

# In[3]:


"""Este programa será capaz de indicarnos el costo del billete de ida y vuelta de un usuario en tren"""
cost_por_kil = 0.63 #USD/Km
dias = int(input("Ingrese la cantidad de días de su viaje: "))
km_recor = float(input("Ingrese los kilómetros aproximados de su recorrrido: "))



if (dias > 7) and (km_recor > 800):
    print ("Tiene descuento del 30%!! ")
    #Costo del boleto
    cost_bill = 0.7 * cost_por_kil * km_recor
    print ("El costo de su boleto es: ", cost_bill)
else: 
    cost_bill = cost_por_kil * km_recor
    print ("El costo de su boleto es: ", cost_bill)
    


# Punto_2  -- SRV 03

# In[8]:


"""Este programa determinará si un año es bisiesto o no"""

year = int(input("Ingrese el año a verificar: "))

if (year % 4) == 0:
    if (year % 100 == 0) and (year % 400 != 0):
        print ("Este año NO es bisiesto")
    else:
        print ("Este año ES bisisesto!!!")
else:
    print ("Este año NO es bisisesto!!!")


# Punto_3 -- SRV 03

# In[12]:


"""Este programa calcula el índice de masa corporal de un usuario mayor de 16 años.
Para esto le solicita al usuario ingresar su peso en libras (lb) y su altura en pulgadas (in)"""

peso = float(input("Ingrese su peso en libras: "))
altura = float(input("Ingrese su altura en pulgadas: "))

#Conversiones del peso a Kilogramos y de la altura a metros.
kg_en_lb =  0.45359237 
peso_en_kg = peso * kg_en_lb
m_en_in = 0.0254
altura_en_m = altura * m_en_in

BMI = peso_en_kg / (altura_en_m ** 2)

if BMI < 18.5:
    print (f"BMI is {BMI:.2f}", "\nBajo peso")   

elif BMI >= 18.5 and BMI <= 24.9:
    print (f"BMI is {BMI:.2f}", "\nNormal")

elif BMI >= 25.0 and BMI <= 29.9:
    print (f"BMI is {BMI:.2f}", "\nSobrepeso")

elif BMI >= 30.0: 
    print (f"BMI is {BMI:.2f}", "\nObeso")


# Punto_5 -- SRV 03

# In[ ]:


"""Este programa determina la cantidad de dígitos de un número"""

num = int(input("Ingrese el número: "))

if num < 10 and num >= 0:
    print ("Input: ", num, "\nOutput: El número tiene 1 dígito")

elif num >= 10 and num < 100:
    print ("Input: ", num, "\nOutput: El número tiene 2 dígitos")
    
elif num >= 100 and num < 1000:
    print ("Input: ", num, "\nOutput: El número tiene 3 dígitos")
    
elif num >= 1000 and num < 10000:
    print ("Input: ", num, "\nOutput: El número tiene 4 dígitos")    

elif num >= 10000 and num <= 100000:
    print ("Input: ", num, "\nOutput: El número tiene 5 dígitos")

elif num > 100000:
    print ("Input: ", num, "\nOutput: El número excede la capacidad del programa")

else:
    print ("Este número es negativo. Ingrese uno positivo")"""Este programa determina la cantidad de dígitos de un número"""

num = int(input("Ingrese el número: "))

if num < 10 and num >= 0:
    print ("Input: ", num, "\nOutput: El número tiene 1 dígito")

elif num >= 10 and num < 100:
    print ("Input: ", num, "\nOutput: El número tiene 2 dígitos")
    
elif num >= 100 and num < 1000:
    print ("Input: ", num, "\nOutput: El número tiene 3 dígitos")
    
elif num >= 1000 and num < 10000:
    print ("Input: ", num, "\nOutput: El número tiene 4 dígitos")    

elif num >= 10000 and num <= 100000:
    print ("Input: ", num, "\nOutput: El número tiene 5 dígitos")

elif num > 100000:
    print ("Input: ", num, "\nOutput: El número excede la capacidad del programa")

else:
    print ("Este número es negativo. Ingrese uno positivo")


# Punto_4 -- SRV 03

# In[ ]:


"""Este programa solicita ingresar un día de la semana y una cantidad de días futuros. 
Al final imprime el día actual y el día futuro."""

day_act = int(input("ingrese el día de la semana actual [0-6]: "))

if day_act == 0:
    print ("Dia actual: Domingo")

elif day_act == 1:
    print ("Dia actual: Lunes")
    
elif day_act == 2:
    print ("Dia actual: Martes")
    
elif day_act == 3:
    print ("Dia actual: Miércoles")
    
elif day_act == 4:
    print ("Dia actual: Jueves")

elif day_act == 5:
    print ("Dia actual: Viernes")

elif day_act == 6:
    print ("Dia actual: Sábado")

day_fut = int(input("ingrese la cantidad de días futuros: "))

diff = abs(day_fut - day_act)
mod = diff % 7

  

if mod == 0:
    day_fut = day_act

else: 
    if (mod + day_act) <= 6:
        day_fut = day_act + mod
    else:
        i = 6 - day_act #Los días que faltan para que termine la semana
        day_fut = mod-i



if day_fut == 0:
    print ("Dia futuro: Domingo")

elif day_fut == 1:
    print ("Dia futuro: Lunes")
    
elif day_fut == 2:
    print ("Dia futuro: Martes")
    
elif day_fut == 3:
    print ("Dia futuro: Miércoles")
    
elif day_fut == 4:
    print ("Dia futuro: Jueves")

elif day_fut == 5:
    print ("Dia futuro: Viernes")

elif day_fut == 6:
    print ("Dia futuro: Sábado") 

else:
    print ("Ha ocurrido un error")
    

    

