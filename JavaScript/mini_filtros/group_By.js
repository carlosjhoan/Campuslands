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
    return (elem[0])
}

const array_prove = [[1, 2, 3], [1, 3, 5], [2, 1], [3, 1, 2]]

console.log(group_By(array_prove, fn));