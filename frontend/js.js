const input = document.getElementById("textInput")
const output = document.getElementById("list")

const env = {
  brands_url: 'http://localhost:8000/api/Brands?text=',
  add_url: 'http://localhost:8000/api/Brands/add?text=', 
  remove_url: 'http://localhost:8000/api/Brands/remove?text='
}

const btn_add = document.getElementById("btn_add")
const btn_remove = document.getElementById("btn_remove")

btn_add.addEventListener("click", addItem)
btn_remove.addEventListener("click", removeItem)

input.oninput = function(){
  generateList(input.value)
}

function generateList(text){
  getItems(text).then(items => {

    output.innerHTML = ""
    for (let i = 0; i < items.length; i++) {
        const listItem = document.createElement("li");
        listItem.appendChild(document.createTextNode(items[i]));
        output.appendChild(listItem);
    }
  })

  
}

const getItems = async (text) => {

    const response = await fetch(env.brands_url + text, {
      method: 'GET',
      mode: 'cors',
      headers: {}
    });
    const myJson = await response.json(); //extract JSON from the http response
    let items = myJson["brands"]
    return items //return the brands
}

generateList("")

// Adding and Removing Items by clicking the buttons:

async function removeItem(){
  if (input.value == "") return;
  const response = await fetch(env.remove_url + input.value, {
    method: 'POST',
    mode: 'cors',
    headers: {}
  });
  const myJson = await response.json(); //extract JSON from the http response
  //TODO: ausgabe status
  console.log(myJson)
  input.value = ""
  generateList(input.value)
}

async function addItem(text){
  if (input.value == "") return;
  const response = await fetch(env.add_url + input.value, {
    method: 'POST',
    mode: 'cors',
    headers: {}
  });
  const myJson = await response.json(); //extract JSON from the http response
  //TODO: ausgabe status
  console.log(myJson)
  generateList(input.value)
}