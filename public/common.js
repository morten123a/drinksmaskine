export async function sendHttpGetRequest(path, data) {
    let query = "";
    let first = true;
    for (const key in data){ //laver en "for" løkke for hver data der er den data der kommer ind
        if (! first){
            query += "&"; //tilføjer et &-tegn i starten af vores query
        }
        first = false;
        query += `${key}=${JSON.stringify(data[key])}`; //tilføjer dataen til query'en, dette gøres sådan da den også skal kunne tage arrays
    }
    const url = path + "?" + query; //tilføjer path og query i en variable
    const response = await fetch(url); //samler det hele sammen og venter på det
    const responseData = await response.json(); //venter på at svaret kommer i json format
    return responseData;
}