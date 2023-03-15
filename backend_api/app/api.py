from fastapi import FastAPI
import backend.backend_api as backend_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="IsThisNestle API",
    description="""This API manages a list of the Brands that Nestle owns""",
    version="0.0.1",
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/Brands')
def Brands(text: str) -> dict:
    """returns all Brands with "text" as substring

    Returns:
        json: list of all Barnds
    """
    
    brands = backend_api.get_brands(text)
    return {'brands': brands}
    
@app.post('/api/Brands/add')
def add_brand(text: str) -> dict:
    """Adds the "brand to the list 

    Args:
        brand (str): the name of the Brand that should be added

    Returns:
        str: status of the Request
    """
    return backend_api.add_brand(text)

@app.post('/api/Brands/remove')
def remove_brand(text: str) -> dict:
    """removes the brand, if ther is any, with the same name as "brand"

    Args:
        brand (str): the brand that should be removed

    Returns:
        str: status iof the Request
    """
    return backend_api.remove_brand(text)

if __name__ == "__main__":
    pass