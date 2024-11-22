import { sendHttpGetRequest } from "./common.js";

const searchdrinks = document.getElementById("drinksSearch");

const checkboxTable = [
    { id: "checkbox-gin", value: "gin" },
    { id: "checkbox-vodka", value: "vodka" },
    { id: "checkbox-rom", value: "rom" },
    { id: "checkbox-mango-sirup", value: "mango sirup" },
    { id: "checkbox-blue-curacao", value: "blue curacao" },
    { id: "checkbox-passionfruit-sirup", value: "passionfruit sirup" },
    { id: "checkbox-grenadine", value: "grenadine" },
    { id: "checkbox-fanta", value: "fanta" },
    { id: "checkbox-cola", value: "cola" },
    { id: "checkbox-schweppes", value: "schweppes" },
    { id: "checkbox-faxe-kondi", value: "faxe kondi" },
    { id: "checkbox-booster", value: "booster" },
    { id: "checkbox-redbull", value: "redbull" },
    { id: "checkbox-æblejuice", value: "æblejuice" },
]

function getActivatedFilters() {
    let filters = []
    for (const { id, value } of checkboxTable) {
        const ischecked = document.getElementById(id).checked;
        if (ischecked) {
            filters.push(value)
        }}
    return filters
}

async function performFilterQuery() {
    searchdrinks.value = "" //Clear search bar
    const filters = getActivatedFilters() //get filters
    const responseData = await sendHttpGetRequest('/mydrinks_filter', {  //Send filter req
        filter: filters, }) // sender en request med navn filtter med filters inputet
    return responseData;
}

function clearAllFilters() {
    for (const { id } of checkboxTable) { //Går igennem alle checkboksene og fjerner ders værdi
        const checkbox = document.getElementById(id);
        if (checkbox) {
            checkbox.checked = false; // Fjern markeringen af checkboksen
}}}

async function performSearchQueryFilter(){ //
    const responseData1 = await sendHttpGetRequest('/search', { //henter dataen med brugerens data og returnere svaret
        search: searchdrinks.value, }) 
    searchdrinks.value = "" //tømmer search baren
    return responseData1
}

const filterslist = document.getElementById("apply-filters");
filterslist.addEventListener('click', async () => {
    performFilterQuery()
    drinksoutput()
});

searchdrinks.addEventListener('keydown', function(event){ //kører det i funktionen når brugeren trykker enter
    if (event.key === 'Enter'){
        clearAllFilters() //fjerner alle filtre
        performSearchQueryFilter() //henter dataen fra serveren
        drinksoutput2() //laver outputet til brugeren
}})

async function drinksoutput() {
    const myoutput = document.getElementById("my-drinks");
    const outputdata = await performFilterQuery()
    myoutput.innerHTML = Object.entries(outputdata)
        .map(([drinkName, ingredientsAndAmounts]) => {
            const ingredientsAndAmountsHtml = ingredientsAndAmounts
                .map(({ingredient, amount}) => {
                    return `
                        <span class="colum">${ingredient} x ${amount}</span>
                    `;})
                .join("");

             return `
                 <div class="drinksoutput">
                     <h3>${drinkName}</h3>
                     <img src="/images/${drinkName}.png" alt=>
                     <div>${ingredientsAndAmountsHtml}</div>
                 </div>
             `;})
        .join("");
}

async function drinksoutput2() {
    const myoutput = document.getElementById("my-drinks");
    const outputdata = await performSearchQueryFilter()
    myoutput.innerHTML = Object.entries(outputdata)
        .map(([drinkName, ingredientsAndAmounts]) => {
            const ingredientsAndAmountsHtml = ingredientsAndAmounts
                .map(({ingredient, amount}) => {
                    return `
                        <span class="colum">${ingredient} x ${amount}</span>
                    `;})
                .join("");
            
             return `
                 <div class="drinksoutput">
                     <h3>${drinkName}</h3>
                     <img src="/images/${drinkName}.png" alt=>
                     <div>${ingredientsAndAmountsHtml}</div>
                 </div>
             `;})
        .join("");
}
