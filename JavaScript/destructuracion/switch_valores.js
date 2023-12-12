let a = 3
let b = 7

//Si no supiéramos de estructuración, cómo hacemos para invertir los valores de a y b

/*let t = b
b = a
a = t*/
console.log(a, b);

[a, b] = [b, a];

console.log(a, b)