

fetch ('http://localhost:4001/usuarios?tipoId=3', {
    method: 'GET',
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))
let data = {
    "id": "2",
    "nombre": " Juan Carlos Aguilar",
    "email": "juanchopolo@gmail.com",
    "cel_num": "3124649852"
}

/*fetch ('http://localhost:3000/orders', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))*/

/*fetch ('http://localhost:3000/trainers/3', {
    method: 'PUT',
    body: JSON.stringify({
        "id": "3",
        "nombre": "Yulieth",
        "apellido": "Rueda",
        "especialidad": "FullStack Python",
        "sexo" : "f",
        "edad" : "20"

    }),
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))

fetch ('http://localhost:3000/trainers/3', {
    method: 'PATCH',
    body: JSON.stringify({
        
        "edad" : "18"

    }),
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))

fetch ('http://localhost:3000/trainers/3', {
    method: 'DELETE',
    
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))*/