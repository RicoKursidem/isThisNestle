from fastapi import FastAPI, Request
import backend.backend as backend_api

app = FastAPI(
    title="IsThisNestle API",
    description="""This API manages a list of the Brands that Nestle owns""",
    version="0.0.1",
    )

@app.get('/api/Brands')
def Brands(text: str) -> str:
    """returns all Brands with "text" as substring

    Returns:
        json: list of all Barnds
    """
    
    brands = backend_api.get_brands(text)
    
    return f'brands: {brands}'
    
@app.post('/api/Brands/add')
def addBrand(brand: str) -> str:
    """Adds the "brand to the list 

    Args:
        brand (str): the name of the Brand that should be added

    Returns:
        str: status of the Request
    """

@app.post('/api/Brands/remove')
def addBrand(brand: str) -> str:
    """removes the brand, if ther is any, with the same name as "brand"

    Args:
        brand (str): the brand that should be removed

    Returns:
        str: status iof the Request
    """
if __name__ == "__main__":
    pass