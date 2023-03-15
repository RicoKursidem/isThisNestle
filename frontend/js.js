const input = document.getElementById("textInput")
const output = document.getElementById("list")



input.oninput = function() {
    items = getItems(input.value);

    output.innerHTML = ""
    for (let i = 0; i < items.length; i++) {
        const listItem = document.createElement("li");
        listItem.appendChild(document.createTextNode(items[i]));
        output.appendChild(listItem);
    }
}

const getItems = async (text) => {
    url = 'http://localhost:8000/api/Brands?text=' + text
    if (text == ""){
      url = 'http://localhost:8000/api/Brands?text'
    }

    const response = await fetch(url, {
      method: 'GET',
      mode: 'cors',
      headers: {}
    });
    const myJson = await response.json(); //extract JSON from the http response
    return myJson
}
