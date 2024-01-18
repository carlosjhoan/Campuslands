import mostrarTexto from "./mostrartexto.js"
import mostrarJSON from "./mostrarjson.js"

// Mostrar texto leyendo CSV
const contenidoTXT = document.getElementById("contenidotexto");
const btnMostrarTXT = document.getElementById("mostrartxt");
btnMostrarTXT.addEventListener("click", e => {
    mostrarTexto(contenidoTXT);
    e.stopPropagation();
});

// Mostrar tabla leyendo JSON
const datTabla = document.getElementById("dattabla");
const btnMostrarJSON = document.getElementById("mostrarjson");
btnMostrarJSON.addEventListener("click", e => {
    mostrarJSON(datTabla);
    e.stopPropagation();
});