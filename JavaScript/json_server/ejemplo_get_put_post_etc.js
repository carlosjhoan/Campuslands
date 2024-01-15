/*fetch ('http://localhost:3000/orders', {
    method: 'GET',
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))*/

fetch ('http://localhost:3000/orders', {
    method: 'POST',
    body: JSON.stringify({
        "id": "0001",
        "name": "Juan Carlos",
        "email" : "juanchopolo@gmail.com"

    }),
    headers: {
        'Content-type' : 'application/json; charset=UTF-8'
    },
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error("ERROR!!!:" + error))

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