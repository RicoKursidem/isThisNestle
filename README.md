# isThisNestle

This is a small Web Development Project to run a List to assist me in not buying Nestle Products. I will run this as an Docker Container on my private Server. Feel free to copy this work and stop buing Nestle too.

## How To Contribute

If there should be Names of Brands that aren't in the List, create an Issue and assign me and I will add these Brands

## How to Run without docker for testing

download all python packages in the requirements.txt into your venv

```bash
pip install -r requirements.txt
```

start the api by navigating to the api.py and executing 

```bash
uvicorn api:app --reload
```

open the index.html in the frontend folder
