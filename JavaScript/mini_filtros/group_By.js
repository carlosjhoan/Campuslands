function group_By (arr, fnct) {
    let obj = {};
    
    arr.forEach( element => {
        if (fnct(element) in obj) {
            
            obj[`${fnct(element)}`].push(element);
            
        } else {
            obj[`${fnct(element)}`] = [element];
            
        }   
    })

    return obj
}

const fn = function (elem) {
    return (elem.id)
}

const array_prove = [{"id" : 1}, {"id" : 1, "nombre" : "juan"}, {"id" : 2, "nombre" : "Carlos Juan"}, {"id" : 2, "nombre" : "Jhon F."}]

console.log(group_By(array_prove, fn));
