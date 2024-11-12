document.getElementById("my-form")
    .addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        console.log(data.get("my-name"))

        const name = data.get("my-name");
        const response = await fetch(`/saymyname?name=${name}`).then(res => res.json());
        console.log(response
        )

    });

document.getElementById("form-recipe")
    .addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = new FormData(e.target);
        console.log(data.get("name"))

        const name = data.get("name");
        const response = await fetch(`/createrecipe?name=${name}`).then(res => res.json());
        console.log(response
        )

    });


async function getRecipies(drinkId) {
    const recipes =
        await fetch(`/get-recipe?drink_id=${drinkId}`)
            .then(res => res.json());
}

