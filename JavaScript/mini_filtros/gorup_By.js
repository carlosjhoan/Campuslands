function group_By (arr, fnct) {
    let obj = {};
    arr.forEach( element => {
        fnct(element)
        
    })
}