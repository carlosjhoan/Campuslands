let arr_per = [];
const main = document.querySelector("main");
main.style.display = "flex";
main.style.flexWrap = "horizontal"
const info_api = fetch("https://rickandmortyapi.com/api/character")
.then (response => response.json())
.then (data => {
    const results = data.results;
    results.forEach(element => {
        const new_div = document.createElement("div");
        new_div.style.display= "flex";
        new_div.style.flexDirection = "column";
        new_div.innerHTML = `<img class='animate animate__hinge' width = "50%" src = ${element.image}><h2>${element.name}</h2><p>${element.status}</p>`
        main.appendChild(new_div)
        
    });
    console.log(results)
    
}
)
console.log(main)




