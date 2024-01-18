const obj = { //objeto
    "empleados": [ //array
        {
            "nombre" : "Juan Pérez",
            "apellido": "López",
            /*nombre_completo: function () {
                return this.nombre + " " + this.apellido
            } Esto si quisiera hacerlo uno ppor uno*/
        },
        {
            "nombre" : "Ana",
            "apellido": "González",
            /*nombre_completo: function () {
                return this.nombre + " " + this.apellido
            }*/
        },
        {
            "nombre" : "Pedro",
            "apellido": "Sánchez",
            /*nombre_completo: function () {
                return this.nombre + " " + this.apellido
            }*/
        }
    ],
    "nombre_completo": function (pos) {
        return this.empleados[pos].nombre + " " + this.empleados[pos].apellido
    }
    
}

console.log(obj.empleados[2].apellido)
//console.log(obj.empleados[2].nombre_completo())
console.log(obj.nombre_completo(2))