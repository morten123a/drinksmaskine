import { sendHttpGetRequest } from "./common.js";

const searchdrinks = document.getElementById("drinksSearch");
searchdrinks.addEventListener('keypress', ()=>{
    const value2 = searchdrinks.value
    console.log(value2)
})

const checkboxTable = [
    { id: "checkbox-gin",                   value: "gin" },
    { id: "checkbox-vodka",                 value: "vodka" },
    { id: "checkbox-rom",                   value: "rom" },
    { id: "checkbox-mango-sirup",           value: "mango sirup" },
    { id: "checkbox-blue-curacao",          value: "blue curacao" },
    { id: "checkbox-passionfruit-sirup",    value: "passionfruit sirup" },
    { id: "checkbox-grenadine",             value: "grenadine" },
    { id: "checkbox-fanta",                 value: "fanta" },
    { id: "checkbox-cola",                  value: "cola" },
    { id: "checkbox-schweppes",             value: "schweppes" },
    { id: "checkbox-faxe-kondi",            value: "faxe kondi" },
    { id: "checkbox-booster",               value: "booster" },
    { id: "checkbox-redbull",               value: "redbull" },
    { id: "checkbox-æblejuice",             value: "æblejuice" },
]

function getActivatedFilters (){
    let filters = []
    for (const {id, value} of checkboxTable){
        const ischecked = document.getElementById(id).checked;
        if (ischecked){
            filters.push(value)
        }
    }
    return filters
}

async function performFilterQuery (){
    //Clear search bar
    searchdrinks.value = ""
    //get filters
    const filters = getActivatedFilters()
    //Send filter req
    const responseData = await sendHttpGetRequest('/mydrinks_filter', {
        filter: filters, 

    })  

    //show results
    console.log(responseData)
}

for (const {id, value} of checkboxTable){
    document.getElementById(id).addEventListener("change", ()=>{
        console.log(getActivatedFilters())
        
    });
}

const filterslist = document.getElementById("apply-filters");
filterslist.addEventListener('click', async () => {
     console.log(getActivatedFilters())
     performFilterQuery()
});

