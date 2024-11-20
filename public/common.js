export async function sendHttpGetRequest(path, data) {
    let query = "";
    let first = true;
    for (const key in data){
        if (! first){
            query += "&";
        }
        first = false;
        query += `${key}=${JSON.stringify(data[key])}`;
    }
    const url = path + "?" + query;
    const response = await fetch(url);
    const responseData = await response.json();
    return responseData;
}