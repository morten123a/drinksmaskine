// document.getElementById("my-form")
//     .addEventListener('submit', async (e) => {
//         e.preventDefault();
//         const data = new FormData(e.target);
//         console.log(data.get("my-name"))

//         const name = data.get("my-name");
//         const response = await fetch(`/saymyname?name=${name}`).then(res => res.json());
//         console.log(response)
//         

//     });
import { sendHttpGetRequest } from "./common.js";

const searchbar = document.getElementById("mySearch");

async function performSearchQuery(){ //laver en fuction til det at lave en search Query
    const responseData1 = await sendHttpGetRequest('/search', {
        // search: searchbar.value,
        search: searchbar.value,
    })
    //tømmer search baren
    searchbar.value = ""
    console.log(responseData1)
    return responseData1;
}

searchbar.addEventListener('keydown', function(event){
    if (event.key === 'Enter'){
        //her skal main function kørers

        performSearchQuery()
        console.log(performSearchQuery())
        drinksoutput()
    }
})

async function drinksoutput() {

    const myoutput = document.getElementById("my-drinks");

    const outputdata = await performSearchQuery()

    console.log(outputdata)    
    for (const drink in outputdata) {
        for (const i in outputdata[drink]) {
        console.log(outputdata[drink][i])
        }
    }

     myoutput.innerHTML = Object.entries(outputdata)
         .map(([drinkName, ingredientsAndAmounts]) => {

             const ingredientsAndAmountsHtml = ingredientsAndAmounts
                 .map(({ingredient, amount}) => {
                     return `
                         <span class="colum">${ingredient} x ${amount}</span>
                     `;
                 })
                 .join("");

             return `
                  <div class="drinksoutput1">
                      <h3>${drinkName}</h3>
                      <img src="/images/${drinkName}.png" alt=>
                      <div>${ingredientsAndAmountsHtml}</div>
                  </div>
              `;
         })
         .join("");
}