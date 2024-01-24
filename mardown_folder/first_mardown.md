# Primer Nivel
## Segundo Nivel
### Tercer nivel
#### Cuarto nivel
##### Quinto nivel
###### Sexto nivel

Hello, I'm Carlos Aguilar, 28 years old, Mechanical Engineer.  
At the moment I'm studying software developer in CampusLands.  
I'd like finished on May.  
***
Hi guys, I'm Camilo, 22 years old, a LGTB.  
***
# Agregar una imagen
How Can I add an image?
![Sabor Casero!](../HTML&CSS/img_proyecto/pickup.png "Sabor Casero")  

# Citar párrafos
Yo puedo generar una cita de la siguiente manera:  
> Esta es la cita que puedo hacer.      

Aquí finalizo la cita

> Esto se puede referenciar de la siguiente manera:
>
>> Por ejemplo, esto viene siendo una cita anidada.  
> 
> Aquí finalizan las citas anidadas.  

# Listas desornadas

- 1er item
- 2do item
    - item 3
    - item 4
- 5to item

# Listas ordenadas
1. 1er item
2. 2do item
    - Item desornado
    - Item desordenado
    1. 3er item
    2. 4to item
3. 5to item

# Bloques de código
`Creando bloque de código.`
`Puedes añadir tantas líneas que quieras`

# Group By Function
***
Write code that enhances all arrays such that you can call the `array.groupBy(fn)` method on any  
array and it will return a ***grouped*** version of the array.  

A ***grouped*** array is an object where each key is the output of `fn(arr[i])` and each value is an array  
containing all items in the original array with that key.  

The provided callback `fn` will accept an item in the array and return a string key.  

The order of each value list should be the other the items appear in the array. Any order of keys is  
acceptable.  

Please solve it without lodash's `_.groupBy` funcytion.  

***Example 1:***  

***input***  

    array = [  
        {"id" : "1"}, 
        {"id" : "1"},
        {"id" : "2"}
    ];
    fn = function (item) {
        return item.id;
    }  

***output:***  

    {
        "1" : [{"id" : "1"}, {"id" : "1"}],
        "2" : [{"id" : "2"}]
    }  

***Explanation:***  

   - Output is from array.groupBy(fn).
   - The selector function gets the "id" out of each item in the array.
   - There are two objects with an "id" of 1. Both of those objects are put in the firstarray.
   - There is one object with and "id" of 2. That object is put in the second array. 


![Imagen](https://external-preview.redd.it/YAmXmXE8z1ilmEMNCxWaOISFuoG0TgZR7caG544jNBM.jpg?auto=webp&s=6b985533b368804ad1611cb3c209c1fd294ee946)

***_cursiva y negrita_***
*__cursiva y negrita__*

<font color = "orange">const</font> MARK = <font color = "green">"DOWN"</font>  

<font color = "orange">for</font> i <font color = "orange">in</font> range(vec):
      print (i)









