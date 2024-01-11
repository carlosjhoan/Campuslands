export default function mostrarJSON(elemHTML) {
    fetch("datos.json")
    .then(data => data.json())
    .then(data2 => {
        console.table(data2);

        dibujarTabla(elemHTML, data2);
    })
}

function dibujarTabla(elemHTML, datos) {
    let tabla = "";
    for(let valor of datos) {
        tabla += `
        <tr>
                <td>${valor.Nombre}</td> 
                <td>${valor.Team}</td>
                <td class="valedad">${valor.Edad}</td> 
                <td class="tdimg">
                    <img 
                        src ='${valor.Sexo === "M" ? "hombre.png": "mujer.png" }'
                        class="imgsexo"
                    />
                </td>   
            </tr>
        
        `
            
    }
    elemHTML.innerHTML= tabla;
}
