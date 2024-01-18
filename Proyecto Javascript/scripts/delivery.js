
let arr_pedido = [["S. de gallina", 0,"i_want_gallina" , "img_check_gallina"],

["S. de costilla", 0, "i_want_costilla" , "img_check_costilla"],

["S. de cola", 0, "i_want_cola" , "img_check_cola"],

["Sobrebarriga", 0, "i_want_sobre" , "img_check_sobre"],

["Chatas", 0, "i_want_chatas" , "img_check_chatas"],

["Oreada",  0, "i_want_ore" , "img_check_ore"],
]

let data = [];
let id_order;
let data_facturas

let total_price;

window.onpageshow = function () {
const inpu_car = document.getElementById("value_order");
inpu_car.value = 0;

fetch ('http://localhost:3000/orders', {
method: 'GET',
headers: {
'Content-type' : 'application/json; charset=UTF-8'
},
})

.then(response => response.json())
.then(json => {
if (json.length == 0) {
id_order = 0;
} else {
id_order = json.length
}

})

}

function vibrate (arr_div_id) {
let d_C = 20;
//const input_element = document.getElementById(div_id);
rotate_animation = setInterval(frame, 20)
function frame () {
for (let i=0; i< arr_div_id.length; i++) {
if (d_C <= -20) {
document.getElementById(arr_div_id[i]).style.translate = "0px";
document.getElementById(arr_div_id[i]).addEventListener("click", () => {
document.getElementById(arr_div_id[i]).style.color = "black";
document.getElementById(arr_div_id[i]).style.backgroundColor = "rgb(254, 236, 236)";
document.getElementById(arr_div_id[i]).style.border = "2px solid";


})

clearInterval(rotate_animation);


} else {
d_C -= 5
document.getElementById(arr_div_id[i]).style.translate = d_C + "px";
document.getElementById(arr_div_id[i]).style.color = "red";
document.getElementById(arr_div_id[i]).value = "Información incorrecta";
document.getElementById(arr_div_id[i]).addEventListener("click", () => {
if (document.getElementById(arr_div_id[i]).value === "Información incorrecta") {
document.getElementById(arr_div_id[i]).value = ""
}
})

}
}

} 

}

function order_buy (div_id, img_id, pos_arr_pedido) {
let table = "<tr><th><b>Cant</b></th><th><b>Plato</b></th><th><b>$/unidad</b></th> <th><b>Valor</b></th><th><b>Cancelar</b></th></tr>";//
const table_order = document.getElementById("table_order");//
let q_orders = 0;
let moneyFormatter  = new Intl.NumberFormat(); 
const id_input = div_id + '_input'
const img_check = document.getElementById(img_id);
const div_proteina = document.querySelector(`#${div_id}`);
const buy_car = document.getElementById("img_car");
const value_order = document.getElementById("value_order");
const but_mi_pedido = document.getElementById("button_mi_pedido");
but_mi_pedido.style.width = "80px";
buy_car.style["background-color"] = "rgb(69, 244, 69)";
value_order.style["background-color"] = "rgb(5, 132, 5)";
value_order.style.border = "1px rgb(5, 132, 5)";
value_order.style.width = "100px";
but_mi_pedido.style.visibility = "visible";
const div_quantity= document.createElement("div");
div_quantity.innerHTML = `<div class = "plus_minus"><button onclick ='minus("${div_id}","${id_input}", "${img_id}", "${pos_arr_pedido}")'>-</button><input type="text" readonly id = ${id_input}>
<button onclick = 'add("${id_input}", "${pos_arr_pedido}")'>+</button></div>`;
for (let i = 0; i<div_proteina.children.length; i++) {
div_proteina.children[i].remove ();
}
img_check.remove();
div_proteina.appendChild(div_quantity);
const input_element = document.getElementById(`${id_input}`);
input_element.style["font-weight"] = "bold";
input_element.value = 1;
input_element.style["text-align"] = "center";
input_element.style.width = "30px";
///////////////////
arr_pedido[pos_arr_pedido][1] = 1;

for (let i = 0; i < arr_pedido.length; i++) {
q_orders += arr_pedido[i][1];
}
total_price = 14000 * q_orders;
console.log("q_orders", q_orders)

value_order.value = `$ ${moneyFormatter.format(total_price)} COP`;
///
for (let i=0; i<arr_pedido.length; i++) {
if (arr_pedido[i][1] > 0) {
table += `<tr><td>${arr_pedido[i][1]}</td><td>${arr_pedido[i][0]}</td><td>$14.000</td><td>$${moneyFormatter.format(arr_pedido[i][1]*14000)}</td><td><button onclick ='cancel_order("${arr_pedido[i][2]}", "${arr_pedido[i][3]}",${arr_pedido.indexOf(arr_pedido[i])})'><img class = "cancel_product" src = "../img_proyecto/close_order.png"></button></td></tr>`; //agregué botón cancelar
}
}
table += `<tr><td>----</td><td>----</td><td>--------</td><td>--------</td></tr><tr><td></td><td></td><td><b>VALOR TOTAL: </b></td><td>$${moneyFormatter.format(total_price)}</td></tr>`; 
table_order.innerHTML = table;

}

function add(id_input, pos_arr_pedido) {
let table = "<tr><th><b>Cant</b></th><th><b>Plato</b></th><th><b>$/unidad</b></th> <th><b>Valor</b></th><th><b>Cancelar</b></th></tr>"; //agregué la opcion cancelar
const table_order = document.getElementById("table_order"); 
let q_orders = 0; 
let moneyFormatter  = new Intl.NumberFormat(); 
const input_quantity = document.getElementById(id_input);
input_quantity.style["font-weight"] = "bold"; 
let quant_number = Number(input_quantity.value);
const value_order = document.getElementById("value_order");
quant_number++;
arr_pedido[pos_arr_pedido][1] = quant_number;
input_quantity.value = `${quant_number}`;
for (let i = 0; i < arr_pedido.length; i++) {
q_orders += arr_pedido[i][1];
}
total_price = 14000 * q_orders;

value_order.value = `$ ${moneyFormatter.format(total_price)} COP`;
//////////////////////
for (let i=0; i<arr_pedido.length; i++) {
if (arr_pedido[i][1] > 0) {
table += `<tr><td>${arr_pedido[i][1]}</td><td>${arr_pedido[i][0]}</td><td>$14.000</td><td>$${moneyFormatter.format(arr_pedido[i][1]*14000)}</td><td><button onclick ='cancel_order("${arr_pedido[i][2]}", "${arr_pedido[i][3]}",${arr_pedido.indexOf(arr_pedido[i])})'><img class = "cancel_product" src = "../img_proyecto/close_order.png"></button></td></tr>`; //agregué botón
}
}
table += `<tr><td>----</td><td>----</td><td>--------</td><td>--------</td></tr><tr><td></td><td></td><td><b>VALOR TOTAL: </b></td><td>$${moneyFormatter.format(total_price)}</td></tr>`
table_order.innerHTML = table;

}

function minus(div_id, id_input, img_id, pos_arr_pedido) {
let table = "<tr><th><b>Cant</b></th><th><b>Plato</b></th><th><b>$/unidad</b></th> <th><b>Valor</b></th><th><b>Cancelar</b></th></tr>";
const table_order = document.getElementById("table_order");
const review_order = document.querySelector(".lista_pedido");
let q_orders = 0;
let moneyFormatter  = new Intl.NumberFormat();
const buy_car = document.getElementById("img_car");
const but_mi_pedido = document.getElementById("button_mi_pedido");
const value_order = document.getElementById("value_order");
const div_proteina = document.querySelector(`#${div_id}`);
const input_quantity = document.getElementById(id_input);
input_quantity.style["font-weight"] = "bold";
let quant_number = Number(input_quantity.value);
quant_number--;
if (quant_number == 0) {
for (let i = 0; i<div_proteina.children.length; i++) {
div_proteina.children[i].remove ();
}
const div_i_want = document.createElement("div");
div_i_want.innerHTML = `<button class = "i_want" onclick="order_buy('${div_id}', '${img_id}', ${pos_arr_pedido})">Yo quiero!</button>
<img src="../img_proyecto/check_order.png" alt="" id = "${img_id}">`;
div_proteina.appendChild(div_i_want);


} else {
input_quantity.value = `${quant_number}`;
}

arr_pedido[Number(pos_arr_pedido)][1] = quant_number;
for (let i = 0; i < arr_pedido.length; i++) {
q_orders += arr_pedido[i][1];
}
if (q_orders == 0) {
total_price = 0;
buy_car.style["background-color"] = "white";
but_mi_pedido.style.visibility = "hidden";
but_mi_pedido.style.width = "30px";
value_order.style["background-color"] = "black";
value_order.style.width = "30px";
value_order.value = 0;
review_order.style.visibility = "collapse";
document.getElementById("first_name").value = "";
document.getElementById("first_name").style.border = "2px solid black";
document.getElementById("first_name").style.color = "black";
document.getElementById("first_name").style.translate = "0px";
document.getElementById("email").value = "";
document.getElementById("email").style.border = "2px solid black";
document.getElementById("email").style.color = "black";
document.getElementById("email").style.translate = "0px";
document.getElementById("cell_number").value = "";
document.getElementById("cell_number").style.border = "2px solid black";
document.getElementById("cell_number").style.color = "black";
document.getElementById("cell_number").style.translate = "0px"

} else {
total_price = 14000 * q_orders;
value_order.value = `$ ${moneyFormatter.format(total_price)} COP`; 
}

for (let i=0; i<arr_pedido.length; i++) {
if (arr_pedido[i][1] > 0) {
table += `<tr><td>${arr_pedido[i][1]}</td><td>${arr_pedido[i][0]}</td><td>$14.000</td><td>$${moneyFormatter.format(arr_pedido[i][1]*14000)}</td><td><button onclick ='cancel_order("${arr_pedido[i][2]}", "${arr_pedido[i][3]}",${arr_pedido.indexOf(arr_pedido[i])})'><img class = "cancel_product" src = "../img_proyecto/close_order.png"></button></td></tr>`
}
}
table += `<tr><td>----</td><td>----</td><td>--------</td><td>--------</td></tr><tr><td></td><td></td><td><b>VALOR TOTAL: </b></td><td>$${moneyFormatter.format(total_price)}</td></tr>`
table_order.innerHTML = table;

}

function dropdown_order () {
let table = "<tr><th><b>Cant</b></th><th><b>Plato</b></th><th><b>$/unidad</b></th> <th><b>Valor</b></th><th><b>Cancelar</b></th></tr>";
let moneyFormatter  = new Intl.NumberFormat();
const review_order = document.querySelector(".lista_pedido");
const table_order = document.getElementById("table_order");
const search_database = document.getElementById("search_orders");
search_database.style.visibility = "hidden";
for (let i=0; i<arr_pedido.length; i++) {
if (arr_pedido[i][1] > 0) {
table += `<tr><td>${arr_pedido[i][1]}</td><td>${arr_pedido[i][0]}</td><td>$14.000</td><td>$${moneyFormatter.format(arr_pedido[i][1]*14000)}</td><td><button onclick ='cancel_order("${arr_pedido[i][2]}", "${arr_pedido[i][3]}",${arr_pedido.indexOf(arr_pedido[i])})'><img class = "cancel_product" src = "../img_proyecto/close_order.png"></button></td></tr>`
}
}
table += `<tr><td>----</td><td>----</td><td>--------</td><td>--------</td></tr><tr><td></td><td></td><td><b>VALOR TOTAL: </b></td><td>$${moneyFormatter.format(total_price)}</td></tr>`;
table_order.innerHTML = table;
review_order.style.visibility = "visible";
}

function collapse_order() {
const review_order = document.querySelector(".lista_pedido")
review_order.style.visibility = "collapse";
const search_database = document.getElementById("search_orders");
search_database.style.visibility = "visible"
}

function confirm_order() {
const i_want = document.getElementsByClassName("button_i_want");
const button_confirm = document.getElementsByClassName("check_buy");
const review_order = document.querySelector(".lista_pedido");
for (let div of i_want) {
div.style.visibility = "hidden";
}
button_confirm[0].style.visibility = "visible";
review_order.style.visibility = "hidden";

}

function cancel_order(div_id, img_id, pos_arr_pedido) {
arr_pedido[pos_arr_pedido][1] = 0; 
let q_orders = 0;
let moneyFormatter  = new Intl.NumberFormat();
const review_order = document.querySelector(".lista_pedido");
const table_order = document.getElementById("table_order");
const buy_car = document.getElementById("img_car");
const but_mi_pedido = document.getElementById("button_mi_pedido");
const value_order = document.getElementById("value_order");
const div_proteina = document.querySelector(`#${div_id}`);
let table = "<tr><th><b>Cant</b></th><th><b>Plato</b></th><th><b>$/unidad</b></th> <th><b>Valor</b></th><th><b>Cancelar</b></th></tr>";


for (let i=0; i<arr_pedido.length; i++) {
if (arr_pedido[i][1] > 0) {
q_orders += arr_pedido[i][1]
table += `<tr><td>${arr_pedido[i][1]}</td><td>${arr_pedido[i][0]}</td><td>$14.000</td><td>$${moneyFormatter.format(arr_pedido[i][1]*14000)}</td><td><button onclick ='cancel_order("${arr_pedido[i][2]}", "${arr_pedido[i][3]}",${arr_pedido.indexOf(arr_pedido[i])})'><img class = "cancel_product" src = "../img_proyecto/close_order.png"></button></td></tr>`; //agregué botón cancelar
}
}
total_price = q_orders * 14000
table += `<tr><td>----</td><td>----</td><td>--------</td><td>--------</td></tr><tr><td></td><td></td><td><b>VALOR TOTAL: </b></td><td>$${moneyFormatter.format(total_price)}</td></tr>`; 
table_order.innerHTML = table;

if (q_orders == 0) {
buy_car.style["background-color"] = "white";
but_mi_pedido.style.visibility = "hidden";
but_mi_pedido.style.width = "30px";
value_order.style["background-color"] = "black";
value_order.style.width = "30px";
value_order.value = 0;
review_order.style.visibility = "collapse";
document.getElementById("first_name").value = "";
document.getElementById("first_name").style.border = "2px solid black";
document.getElementById("first_name").style.color = "black";
document.getElementById("first_name").style.translate = "0px";
document.getElementById("email").value = "";
document.getElementById("email").style.border = "2px solid black";
document.getElementById("email").style.color = "black";
document.getElementById("email").style.translate = "0px";
document.getElementById("cell_number").value = "";
document.getElementById("cell_number").style.border = "2px solid black";
document.getElementById("cell_number").style.color = "black";
document.getElementById("cell_number").style.translate = "0px"
const search_database = document.getElementById("search_orders");
//search_database.style.visibility = "visible";

} else {
total_price = 14000 * q_orders;
value_order.value = `$ ${moneyFormatter.format(total_price)} COP`; 
}

for (let i = 0; i<div_proteina.children.length; i++) {
div_proteina.children[i].remove ();
}
const div_i_want = document.createElement("div");
div_i_want.innerHTML = `<button class = "i_want" id = "but_oreada" onclick="order_buy('${div_id}', '${img_id}', ${pos_arr_pedido})">Yo quiero!</button>
<img src="../img_proyecto/check_order.png" alt="" id = "${img_id}">`;
div_proteina.appendChild(div_i_want);
console.log(div_id)

}

function previous() {
const i_want = document.getElementsByClassName("button_i_want");
const list_order = document.querySelector(".lista_pedido");
const order_form = document.querySelector(".check_buy");
list_order.style.visibility = "visible";
order_form.style.visibility = "collapse";
for (let div of i_want) {
div.style.visibility = "visible";
}

}


function ok_my_order () {

let review_table = "";
let arr_final_order = [];
let moneyFormatter  = new Intl.NumberFormat();
const regex_name = /^[a-zA-Z\s]+$/; //Para comprobar nombres
const regex_whitespace = /\S/; //Regex para comprobar que no esté vacío
const regex_cel = /^[0-9]+$/; //regex para comprobar el número de teléfono
const regex_email = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g; //reex para comprobar el email
const regex_address = /^[#.0-9a-zA-Z\s,-]+$/; //reex para comprobar la dirección
let arr_divs_verification = []; //Divs para verificar
let arr_divs_id = []; //Array para llenar con los Id's de divs que van a moverse
let arr_true_false = []; //Array para ubicar las verificaciones, False o True
const confirm_div = document.querySelector(".check_buy");
const review_order_div = document.getElementById("review_order");
const children_confirm = confirm_div.childNodes[3].childNodes;

for ( let i= 0; i <children_confirm.length; i++) {

if (children_confirm[i].nodeName == "DIV") {

arr_divs_verification.push([children_confirm[i].childNodes[3].id, children_confirm[i].childNodes[3].value]);

}
}
arr_true_false = [[arr_divs_verification[0][0], Boolean(regex_whitespace.test(arr_divs_verification[0][1])*regex_name.test(arr_divs_verification[0][1]))],
         [arr_divs_verification[1][0], regex_email.test(arr_divs_verification[1][1])],
         [arr_divs_verification[2][0], regex_cel.test(arr_divs_verification[2][1])],
         [arr_divs_verification[3][0], Boolean(regex_whitespace.test(arr_divs_verification[3][1])*regex_address.test(arr_divs_verification[3][1]))]]

arr_true_false.forEach((elem) => {
if (elem[1] == false) {
arr_divs_id.push(elem[0])
}
})
if (arr_divs_id.length >0) {
vibrate (arr_divs_id);
} else {
let now = new Date();
id_order++;
review_table = `<b>N° Factura:</b> ${id_order}<br>
<b>Nombre:</b> ${arr_divs_verification[0][1]}<br>
<b>Email:</b> ${arr_divs_verification[1][1]}<br>
<b>Celular:</b> ${arr_divs_verification[2][1]}<br>
<b>Dirección:</b> ${arr_divs_verification[3][1]}<br>
<b>Observaciones:</b> <em>${document.getElementById("commit").value}</em><br>
<b>Pedido:</b><br>` 
for (let k = 0; k<arr_pedido.length; k++) {
if (arr_pedido[k][1] > 0) {
arr_final_order.push(arr_pedido[k].slice(0,2));
review_table += `-- ${arr_pedido[k][1]}  ${arr_pedido[k][0]}<br>`;
//arr_pedido[k][1] = 0;
}
}

alert("Pedido registrado con éxito!");
review_table += `<b>Precio:</b> $${moneyFormatter.format(total_price)} COP<br><b>Fecha:</b> ${now.toLocaleString()}<br>`
document.getElementById("review_paragraph").innerHTML = review_table;
review_order_div.style.visibility = "visible";
confirm_div.style.visibility = "hidden";
document.getElementById("button_mi_pedido").style.visibility = "hidden";


//Montar el pedido en la base de datos
data = {
"id" : `${id_order}`,
"name" : `${arr_divs_verification[0][1]}`,
"email" : `${arr_divs_verification[1][1]}`,
"celular" : `${arr_divs_verification[2][1]}`,
"direccion" : `${arr_divs_verification[3][1]}`,
"observaciones" : `${document.getElementById("commit").value}`,
"pedido" : arr_final_order,
"precio" : moneyFormatter.format(total_price),
"modo" : "delivery",
"Fecha" : `${now.toLocaleString()}`
}



//---------------------------------


}

}

function finish () {
document.getElementById("review_paragraph").innerHTML = "";
document.getElementById("review_order").style.visibility = "hidden";
document.getElementById("first_name").value = "";
document.getElementById("email").value = "";
document.getElementById("cell_number").value = "";
document.getElementById("dir").value = "";
document.getElementById("commit").value = "";
const search_database = document.getElementById("search_orders");
            search_database.style.visibility = "visible";

const divs_i_want = document.querySelectorAll(".button_i_want");
const buy_car = document.getElementById("img_car");
const but_mi_pedido = document.getElementById("button_mi_pedido");
const value_order = document.getElementById("value_order");

arr_pedido.forEach((elem) => {
if (elem[1] > 0) {
document.getElementById(elem[2]).innerHTML = `<button class = "i_want" id = "but_oreada" onclick="order_buy('${elem[2]}', '${elem[3]}', ${arr_pedido.indexOf(elem)})">Yo quiero!</button>
<img src="../img_proyecto/check_order.png" alt="" id = "${elem[3]}">`;
elem[1] = 0;
}

})

for (let div of divs_i_want) {
div.style.visibility = "visible";
}

buy_car.style["background-color"] = "white";
but_mi_pedido.style.visibility = "hidden";
but_mi_pedido.style.width = "30px";
value_order.style["background-color"] = "black";
value_order.style.width = "30px";
value_order.value = 0;



//Montar en la base de datos
fetch ('http://localhost:3000/orders', {
method: 'POST',
body: JSON.stringify(data),
headers: {
'Content-type' : 'application/json; charset=UTF-8'
},
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))
}

/*BUSCAR EN LA BASE DE DATOS*/

document.getElementById("search_orders").addEventListener("click", () => {
let query;
const regex_info = /^[0-9]+$/; //solo numeros
const button_mi_pedido = document.getElementById("button_mi_pedido");
button_mi_pedido.style.visibility = "hidden";
const option = document.getElementById("option_search").value;
const input_info = document.getElementById("input_database").value;
if (option == "id") {
query = `http://localhost:3000/orders?id=${input_info}`
} else {
query = `http://localhost:3000/orders?celular=${input_info}`
}
fetch (query, {
method: 'GET',
headers: {
'Content-type' : 'application/json; charset=UTF-8'
},
})
.then(response => response.json())
.then(json => {

let num_pos = 0;
let factura = "";
const div_list = document.getElementById("each_order");
const table_orders = document.querySelector(".info_database");
const close_order = document.getElementById("close_order");
const before_order = document.getElementById("before_order");
const after_order = document.getElementById("after_order");
table_orders.style.visibility = "visible";
close_order.style.visibility = "visible";

/*Permitir que el botón close cierre*/
close_order.addEventListener("click", () => {
console.log(total_price)
table_orders.style.visibility = "hidden"
close_order.style.visibility = "hidden";
before_order.style.visibility = "hidden";
after_order.style.visibility = "hidden";
document.getElementById("input_database").value = "";
if (total_price > 0) {
button_mi_pedido.style.visibility = "visible";
} else if (total_price === 0) {
button_mi_pedido.style.visibility = "hidden";
}
})

/*Permitir que el botón hacia ADELANTE funcione*/
after_order.addEventListener("click", () => {
num_pos++;
if (num_pos >= json.length - 1) {
after_order.style.visibility = "hidden";
before_order.style.visibility = "visible";

factura = `<b>N° Factura:</b> ${json[num_pos].id}<br>
                            <b>Nombre:</b> ${json[num_pos].name}<br>
                            <b>Email:</b> ${json[num_pos].email}<br>
                            <b>Celular:</b> ${json[num_pos].celular}<br>`;
                            
                            
if (json[num_pos].modo == "pickup") {
        factura += `<b>Hora recoger:</b> ${json[num_pos].hora}<br>`;
} else {
        factura += `<b>Direccion:</b> ${json[num_pos].direccion}<br>`;
}
    
factura += `<b>Observaciones:</b> <em>${json[num_pos].observaciones}</em><br>
                            <b>Pedido:</b><br>`;

for (let k = 0 ; k < json[num_pos].pedido.length; k++) {
factura += `-- ${json[num_pos].pedido[k][1]} ${json[num_pos].pedido[k][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[num_pos].precio} COP<br>
        <b>modo:</b> ${json[num_pos].modo}<br>
        <b>Fecha:</b> ${json[num_pos].Fecha}<br>`;

div_list.innerHTML =factura;

num_pos = json.length - 1;


} else {
before_order.style.visibility = "visible";
factura = `<b>N° Factura:</b> ${json[num_pos].id}<br>
                            <b>Nombre:</b> ${json[num_pos].name}<br>
                            <b>Email:</b> ${json[num_pos].email}<br>
                            <b>Celular:</b> ${json[num_pos].celular}<br>`;
                            
                            
if (json[num_pos].modo == "pickup") {
        factura += `<b>Hora recoger:</b> ${json[num_pos].hora}<br>`;
} else {
        factura += `<b>Direccion:</b> ${json[num_pos].direccion}<br>`;
}
    
factura += `<b>Observaciones:</b> <em>${json[num_pos].observaciones}</em><br>
                            <b>Pedido:</b><br>`;
for (let k = 0 ; k < json[num_pos].pedido.length; k++) {
factura += `-- ${json[num_pos].pedido[k][1]} ${json[num_pos].pedido[k][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[num_pos].precio} COP<br>
        <b>modo:</b> ${json[num_pos].modo}<br>
        <b>Fecha:</b> ${json[num_pos].Fecha}<br>`;

div_list.innerHTML =factura;

}

})

/*Permitir que el botón hacia ATRÁS funcione*/
before_order.addEventListener("click", () => {
num_pos--;
if (num_pos <= 0) {
before_order.style.visibility = "hidden";
after_order.style.visibility = "visible";

factura = `<b>N° Factura:</b> ${json[num_pos].id}<br>
                            <b>Nombre:</b> ${json[num_pos].name}<br>
                            <b>Email:</b> ${json[num_pos].email}<br>
                            <b>Celular:</b> ${json[num_pos].celular}<br>`;
                            
                            
if (json[num_pos].modo == "pickup") {
        factura += `<b>Hora recoger:</b> ${json[num_pos].hora}<br>`;
} else {
        factura += `<b>Direccion:</b> ${json[num_pos].direccion}<br>`;
}
    
factura += `<b>Observaciones:</b> <em>${json[num_pos].observaciones}</em><br>
                            <b>Pedido:</b><br>`;

for (let j = 0 ; j < json[num_pos].pedido.length; j++) {
factura += `-- ${json[num_pos].pedido[j][1]} ${json[num_pos].pedido[j][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[num_pos].precio} COP<br>
        <b>modo:</b> ${json[num_pos].modo}<br>
        <b>Fecha:</b> ${json[num_pos].Fecha}<br>`;

div_list.innerHTML =factura;

num_pos = 0;
} else {
after_order.style.visibility = "visible";
factura = `<b>N° Factura:</b> ${json[num_pos].id}<br>
                            <b>Nombre:</b> ${json[num_pos].name}<br>
                            <b>Email:</b> ${json[num_pos].email}<br>
                            <b>Celular:</b> ${json[num_pos].celular}<br>`;
                            
                            
if (json[num_pos].modo == "pickup") {
        factura += `<b>Hora recoger:</b> ${json[num_pos].hora}<br>`;
} else {
        factura += `<b>Direccion:</b> ${json[num_pos].direccion}<br>`;
}
    
factura += `<b>Observaciones:</b> <em>${json[num_pos].observaciones}</em><br>
                            <b>Pedido:</b><br>`;

for (let j = 0 ; j < json[num_pos].pedido.length; j++) {
factura += `-- ${json[num_pos].pedido[j][1]} ${json[num_pos].pedido[j][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[num_pos].precio} COP<br>
        <b>modo:</b> ${json[num_pos].modo}<br>
        <b>Fecha:</b> ${json[num_pos].Fecha}<br>`;

div_list.innerHTML =factura;

}

})




if (json.length == 0 || regex_info.test(input_info) == false ) {
div_list.innerHTML = "<em>NO HAY INFORMACIÓN PARA MOSTRAR</em>";
before_order.style.visibility = "hidden";
after_order.style.visibility = "hidden";
} else if (json.length === 1) {

document.getElementById("before_order").style.visibility = "hidden";
document.getElementById("after_order").style.visibility = "hidden";
factura = `<b>N° Factura:</b> ${json[0].id}<br>
                            <b>Nombre:</b> ${json[0].name}<br>
                            <b>Email:</b> ${json[0].email}<br>
                            <b>Celular:</b> ${json[0].celular}<br>`;
                            
                            
                    if (json[0].modo == "pickup") {
                            factura += `<b>Hora recoger:</b> ${json[0].hora}<br>`;
                    } else {
                            factura += `<b>Direccion:</b> ${json[0].direccion}<br>`;
                    }
                        
                    factura += `<b>Observaciones:</b> <em>${json[0].observaciones}</em><br>
                                                <b>Pedido:</b><br>`;

for (let i = 0 ; i < json[0].pedido.length; i++) {
factura += `-- ${json[0].pedido[i][1]} ${json[0].pedido[i][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[0].precio} COP<br>
    <b>modo:</b> ${json[0].modo}<br>
    <b>Fecha:</b> ${json[0].Fecha}<br>`;

div_list.innerHTML =factura;

} else {
console.log(json);
before_order.style.visibility = "hidden";
after_order.style.visibility = "visible";
factura = `<b>N° Factura:</b> ${json[0].id}<br>
                            <b>Nombre:</b> ${json[0].name}<br>
                            <b>Email:</b> ${json[0].email}<br>
                            <b>Celular:</b> ${json[0].celular}<br>`;
                            
                            
                    if (json[0].modo == "pickup") {
                            factura += `<b>Hora recoger:</b> ${json[0].hora}<br>`;
                    } else {
                            factura += `<b>Direccion:</b> ${json[0].direccion}<br>`;
                    }
                        
                    factura += `<b>Observaciones:</b> <em>${json[0].observaciones}</em><br>
                                                <b>Pedido:</b><br>`;

for (let m = 0 ; m < json[0].pedido.length; m++) {
factura += `-- ${json[0].pedido[m][1]} ${json[0].pedido[m][0]}<br>`;
}

factura += `<b>Precio:</b> $${json[0].precio} COP<br>
    <b>modo:</b> ${json[0].modo}<br>
    <b>Fecha:</b> ${json[0].Fecha}<br>`;

div_list.innerHTML =factura;
}


})


})

document.getElementById("stack_icon").addEventListener("mouseover", () => {
if (total_price == 0) {
document.getElementById("search_orders").style.visibility = "visible";
} 
})