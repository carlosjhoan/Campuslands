console.log("Holita")
console.log("*\n**\n***\n****\n*****\n")
console.log("\t*  ***** \n\t* *     *\n\t* *       \n\t*  ***** \n*\t*       *\n*\t* *     *\n ******    ***** ")
//alert ("Holita")

//Comentarios de una sola línea
/*Este
es un comentario multilínea*/

// JS es de tipado dinpámico y débil
x = 32
where_Ani = "Santa"
console.log(x)
/*Todo lo que pueda úselo con variable tipo const*/

//declarar una variable
let mensaje
console.log(typeof(mensaje)) //Me dice qué tipo de variable es
// con let nop se puede declarar la misma variable

//Pero si yo acá le declaro el valor
let a = "Holita"
console.log(typeof(a)) 

//Colocar espacios en la consola
console.log(typeof(a)) +" " + console.log(typeof(mensaje))

//Puedo declarar varias variables de la siguiente forma
let b = 1, c = "Manuel", age = "25", temperature = 15.5

//Qué pasa si divido un entero entre un número
alert ( "holita" / 3)

//Si defino un número batsante grande
m = 65416543534654654354654654654564n
console.log(typeof(m))

//Con los strings
let str = "Holota"
let str2 = "hololita"
let str3 = `Este es otro ${str}` //Concatena
console.log(str3) 

//Booleanos
let plena = true
let mala_plena = false

//null
let f = null 

//ejercicio
let name = "Ilya"
alert (`hola ${1}`)
alert (`hola ${"name"}`)

//Cómo hacer para definir variables globales dentro de los condicionales

if (true) {
    var test = "sí"
}

alert (test) /*test actúa como variable global, pero si en su lugar usamos let dentro del if, entonces el alert no pasa error*/

//OPERADORES
let num_1 = 5
let num_2 = num_1 ++
console.log(num_1)
console.log(num_2)

//depende mucho de dónde está el ++
num_2 = ++num_1 //aquí num_2 vale 7 y num_1 también vale 7 
console.log(num_2)
console.log(num_1)

//&& and
//|| or
//! not
//!= diferente

//ASIGNACIONES
b = 2
a = 5
a **= b //--> esto da a = 25

//Operadores de comparación
/*tenemos 2 opoeradores de igualdad que son:
== es un igual, pero habla más de apariencia, por ejemplo 3 == "3" esto esverdadero
=== es un estrictamente igual (recomendado), este además del valor, revisa que sean el mismo tipo de dato*/

/*LOS VALORES FALSOS
- 0
- -0
- ""
- null
- undefined
- NaN
- false*/

/*LOS VALORES VERDADEROS
- true
- 1
- []
- {}
.
.
.
*/

/*Operadores de cadenas
- Concatenación
- template string
- template liertals
- Métodos string
*/

let cad_1 = "Aprendiendo JS"
let cad_2 = "Con Campus"
let cad_3 = "Holita"
console.log(cad_1 + cad_2) + console.log(cad_2) +console.log(cad_3)

/*Métodos string
console.log(cadena.repeat(number_repetitions))*/
console.log("*".repeat(10))

//startsWith(str, index) -> Empieza con

str = "Hola estoy aprendiendo JavaScript"
console.log(str.startsWith("Hola"))

//endsWith (str, index --> Hace lo contrario a startsWith

//includes(str, index) --> Indica si la cadena incluye la str a partir del index

//prompt: para recibir valores del usuario. Esto recibe cadenas

resultado = prompt("Ingrese la edad: ", 18) // si le damos 'cancel' nos queda null

let is_Boss = confirm("Tú eres el jefe?")
console.log(is_Boss)

//CONVERSIÓN DE DATOS

let value = true
alert (typeof value)
value = String(value)
alert (typeof value)

//Si yo tratoi de hacer la división entre cadenas, pero el contenido de las cadenas es número, JS me lo hace.

console.log("6"/"2")

//Puedo convertir de string  a número

str = "123"
str = Number(str)
console.log(str)
console.log(typeof str)

num_1 = prompt("Digite un número:")
num_2 = prompt ("digite otro número: ")
num_1 = Number(num_1)
num_2 = Number(num_2)
suma= num_1 + num_2;
resta = num_1 - num_2
mult = num_1 * num_2
div = num_1 /num_2
alert(`Suma = ${suma}\nResta = ${resta}\nmultiplicación = ${mult}\nDivisión = ${div}`)
console.log(`Suma = ${suma}\nResta = ${resta}\nmultiplicación = ${mult}}\nDivisión = ${div}`)



