import { sendHttpGetRequest } from "./common.js";

const searchbar = document.getElementById("mySearch");

async function performSearchQuery(){ //laver en fuction til det at lave en search Query
    const responseData1 = await sendHttpGetRequest('/search', {
        search: searchbar.value, })
    searchbar.value = "" //tømmer search baren
    return responseData1;
}

searchbar.addEventListener('keydown', function(event){ //kører det i funktionen når brugeren trykker enter
    if (event.key === 'Enter'){
        performSearchQuery()//henter dataen fra serveren
        drinksoutput()//laver outputet til brugeren
}})

async function drinksoutput() {
    const myoutput = document.getElementById("my-drinks");
    const outputdata = await performSearchQuery()  
    myoutput.innerHTML = Object.entries(outputdata)
         .map(([drinkName, ingredientsAndAmounts]) => {
             const ingredientsAndAmountsHtml = ingredientsAndAmounts
                 .map(({ingredient, amount}) => {
                     return `
                         <span class="colum">${ingredient} x ${amount}</span>
                     `;})
                 .join("");

             return `
                  <div class="drinksoutput1">
                      <h3>${drinkName}</h3>
                      <img src="/images/${drinkName}.png" alt=>
                      <div>${ingredientsAndAmountsHtml}</div>
                  </div>
              `;})
         .join("");
}