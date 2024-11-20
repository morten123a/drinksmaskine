export async function sendHttpGetRequest(path) {
    const response = await fetch(path);
    const data = await response.json();
    return data;
}