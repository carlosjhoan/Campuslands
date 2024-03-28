let a = 1E2;
let b = Number("Hola");
let c = "Hola\vCarlos"
let d = "c" + "a" + "t";
console.log(a);
console.log(isNaN(b));
console.log(c);
console.log("Concatenation:", d);

// differences between let and var
function var_function() {
    var x = 1;
    if (true) {
        var x = 2;
        console.log("x_var if:", x);
    }
    console.log("x_var function:", x);
}

var_function();

function let_function() {
    let x = 1;
    if (true) {
        let x = 2;
        console.log("x_let if:", x);
    }
    console.log("x_let function:", x);
}

let_function();


/* The falsy values in JavaScript
    - false
    - null
    - undefined
    - The empty string ''
    - The number 0
    - The number NaN
*/

// Switch Case
let day;
let date_now = new Date().getDay(); // returns a number between 0 and 6
switch (date_now) {
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;

    case 2:
        day = "Tuesday";
        break;
    
    case 3:
        day = "Wednesday";
        break;
    
    case 4:
        day = "Thursday";
        break;

    case 5:
        day = "Friday";
        break;

    case 6:
        day = "Sunday";
}

console.log("Dayweek:", day);