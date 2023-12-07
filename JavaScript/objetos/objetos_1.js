const persona = {
    nombre : 'Dani',
    apellido: 'Aguilar',
    edad : 30,
    es_trabajador : true,
    familia : ["Miguel", "María"],
    direccion : {
        calle : "Los estudiantes",
        numero : 13,
        ciudad : "Bucaramanga"
    },
    caminar: function () {
        console.log('Estoy caminando')
    },
    nombre_persona: function (){
        return this.nombre + this.apellido //this hace referencia a sí mismo
    }
}

//Acceder a las oropiedades y métodos
console.log(persona.nombre)
console.log(persona.es_trabajador)
persona.caminar()

//Si quiero cambiarle el nombre
persona.nombre = "Daniela"

//Cómo convierto a JSON
const cadena_JSON = JSON.stringify(persona) 
console.log(cadena_JSON) //Me devuelve una cadena

//Cómo convierto un JSOn en objeto
const obj_Per = JSON.parse(cadena_JSON) 
