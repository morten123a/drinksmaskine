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

const searchbar = document.getElementById("mySearch");
    searchbar.addEventListener('keypress', ()=>{
    const value = searchbar.value
    console.log(value)
})