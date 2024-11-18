// document.getElementById("my-form")
//     .addEventListener('submit', async (e) => {
//         e.preventDefault();
//         const data = new FormData(e.target);
//         console.log(data.get("my-name"))

//         const name = data.get("my-name");
//         const response = await fetch(`/saymyname?name=${name}`).then(res => res.json());
//         console.log(response
//         )

//     });

// const searchbar = document.getElementById("mySearch");
// searchbar.addEventListener('keypress', ()=>{
//     const value = searchbar.value
//     console.log(value)
// })'
const checkboxTable = [
    { id: "checkbox-gin",                   value: "gin" },
    { id: "checkbox-vodka",                 value: "vodka" },
    { id: "checkbox-rom",                   value: "rom" },
    { id: "checkbox-mango-sirup",           value: "mango-sirup" },
    { id: "checkbox-blue-curacao",          value: "blue-curacao" },
    { id: "checkbox-passionfruit-sirup",    value: "passionfruit-sirup" },
    { id: "checkbox-grenadine",             value: "grenadine" },
    { id: "checkbox-fanta",                 value: "fanta" },
    { id: "checkbox-cola",                  value: "cola" },
    { id: "checkbox-schweppes",             value: "schweppes" },
    { id: "checkbox-faxe-kondi",            value: "faxe-kondi" },
    { id: "checkbox-booster",               value: "booster" },
    { id: "checkbox-redbull",               value: "redbull" },
    { id: "checkbox-æblejuice",             value: "æblejuice" },
]


let activatedFilters = []

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

for (const {id, value} of checkboxTable){
    document.getElementById(id).addEventListener("change", ()=>{
        console.log(getActivatedFilters())
        activatedFilters = getActivatedFilters()
    });
}


const filterslist = document.getElementById("apply-filters");
    filterslist.addEventListener('click', () => {
     console.log(getActivatedFilters())
})

