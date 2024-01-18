
let info_id;

window.onpageshow = function () {
    

    fetch ('http://localhost:3000/info_users', {
        method: 'GET',
        headers: {
            'Content-type' : 'application/json; charset=UTF-8'
        },
    })

    .then(response => response.json())
    .then(json => {
        if (json.length == 0) {
            info_id = 0;
        } else {
            info_id = json.length
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


document.getElementById("but_submit").addEventListener("click", () => {
    const regex_name = /^[a-zA-Z\s]+$/; //Para comprobar nombres
    const regex_whitespace = /\S/; //Regex para comprobar que no esté vacío
    const regex_cel = /^[0-9]+$/; //regex para comprobar el número de teléfono
    const regex_email = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g; //reex para comprobar el email
    let data; //Para llenar los datos del formulario y subirlo en el json
    let arr_id_input = []; //Arraya para poner el id y la respuesta de validación
    let arr_divs_id = []; //Array para llenar con los Id's de divs que van a moverse
    const name_value = document.getElementById("nombre").value;
    const email_value = document.getElementById("email").value;
    const celular_value = document.getElementById("celular").value;
    let arr_divs_verification = []; //Divs para verificar;
    const now = new Date();

    arr_id_input = [["nombre", Boolean(regex_whitespace.test(name_value)*regex_name.test(name_value))],
                    ["email", regex_email.test(email_value) ] ,
                    ["celular", regex_cel.test(celular_value)] ];

    arr_id_input.forEach((elem) => {
        if (elem[1] == false) {
            arr_divs_id.push(elem[0])

        }
    })

    if (arr_divs_id.length >0) {
        vibrate (arr_divs_id);
        if (document.getElementById("commit").value == "" || document.getElementById("commit").value == "Agradecemos nos escriba algo" || Boolean(regex_whitespace.test(document.getElementById("commit").value))) {
            document.getElementById("commit").value = "Agradecemos nos escriba algo";
            document.getElementById("commit").style.color = "red";
        }
    } else {
        if (document.getElementById("commit").value == "" || document.getElementById("commit").value == "Agradecemos nos escriba algo" || Boolean(regex_whitespace.test(document.getElementById("commit").value)) == false) {
            document.getElementById("commit").value = "Agradecemos nos escriba algo";
            document.getElementById("commit").style.color = "red";
        } else {
            alert("Perfecto! Hemos recibido tu información");
            data = {
                "id" : `${info_id + 1}`,
                "nombre" : `${document.getElementById("nombre").value}`,
                "email" : `${document.getElementById("email").value}`,
                "celular" : `${document.getElementById("celular").value}`,
                "motivo" : `${document.getElementById("options").value}`,
                "contenido" : `${document.getElementById("commit").value}`,
                "hora" : `${now.toLocaleString()}`
            }
            document.getElementById("nombre").value = "";
            document.getElementById("email").value = "";
            document.getElementById("celular").value = "";
            document.getElementById("commit").value = "";
        }
       
    }

    //Montar en la base de datos
    fetch ('http://localhost:3000/info_users', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-type' : 'application/json; charset=UTF-8'
            },
        })
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(error => console.error("ERROR!!!:" + error))

    
})


document.getElementById("commit").addEventListener ("click", () => {
    document.getElementById("commit").style.color = "black";
    if  (document.getElementById("commit").value === "Agradecemos nos escriba algo") {
        document.getElementById("commit").value = "";
    }
})
