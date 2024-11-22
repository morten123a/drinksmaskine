import { sendHttpGetRequest } from "./common.js";

const searchdrinks = document.getElementById("drinksSearch");
searchdrinks.addEventListener('keypress', () => {
    const value2 = searchdrinks.value
    console.log(value2)
})

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
        }
    }
    return filters
}

async function performFilterQuery() {
    //Clear search bar
    searchdrinks.value = ""
    //get filters
    const filters = getActivatedFilters()
    //Send filter req
    const responseData = await sendHttpGetRequest('/mydrinks_filter', {
        filter: filters,

    })

    //show results
    return responseData;
}


for (const { id, value } of checkboxTable) {
    document.getElementById(id).addEventListener("change", () => {
        console.log(getActivatedFilters())

    });
}

const filterslist = document.getElementById("apply-filters");
filterslist.addEventListener('click', async () => {
    console.log(getActivatedFilters())
    performFilterQuery()
    drinksoutput()
});

// inside html 
//  <div id="my-div"></div>

async function drinksoutput() {


    const myoutput = document.getElementById("my-drinks");

    const outputdata = await performFilterQuery()

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
                 <div class="drinksoutput">
                     <h3>${drinkName}</h3>
                     <img src="/images/${drinkName}.png" alt=>
                     <div>${ingredientsAndAmountsHtml}</div>
                 </div>
             `;
        })
        .join("searchdrinks");
}


// inside html
//  <div id="my-div">
//      <div class="player" id="player-4">
//          <p1>name is jeppe and lvl is 44</p1>
//      </div>
//      <div class="player" id="player-22">
//          <p1>name is jeppe and lvl is 34</p1>
//      </div>
//      <div class="player" id="player-213123">
//          <p1>name is morben and lvl is 9</p1>
//      </div>
//  </div>
