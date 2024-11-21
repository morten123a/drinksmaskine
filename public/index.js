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

async function performSearchQuery(){
    const responseData1 = await sendHttpGetRequest('/search', {
        // search: searchbar.value,
        search: searchbar.value,
    })
    searchbar.value = ""
    console.log(responseData1)
}

searchbar.addEventListener('keydown', function(event){
    const value = searchbar.value
    if (event.key === 'Enter'){
        //her skal main function kørers

        performSearchQuery()
        console.log(performSearchQuery())
    }
})