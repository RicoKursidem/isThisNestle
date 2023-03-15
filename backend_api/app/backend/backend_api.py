from backend import file_handler

def main():
    pass

def is_substring_of(string, substring) -> bool:
    """returns True, if the substring is a substring of string

    Args:
        string (str): main string
        substring (str): the substring to test against

    Returns:
        bool: returns if the substring is a substring of string :)
    """
    if substring.lower() in string.lower():
        return True
    
    if "é" in string:
        string = string.replace("é", "e")
        if substring.lower() in string.lower():
            return True
        
    if "'" in string:
        string_ = string.replace("'", " ")
        if substring.lower() in string_.lower():
            return True
        string_ = string.replace("'", "")
        if substring.lower() in string_.lower():
            return True
    
    #TODO: More QOL Stuff
    
    return False

def get_brands(text: str):
    
    brands = file_handler.get_list()
    ret_Brands = []
    
    for brand in brands:
        if is_substring_of(brand, text):
            ret_Brands.append(brand)
    
    return ret_Brands

def add_brand(brand : str) -> dict:
    """_summary_

    Args:
        brand (str): _description_

    Returns:
        dict: _description_
    """
    brands = file_handler.get_list()
    
    if brand in brands:
        return {
            'status': 304, 
            'status-text': "Not Modified - Brand alredy exsists"
        }
    
    brands.append(brand)
    if file_handler.write_list(brands):
        return {
            'status': 500,
            'status-text': "Internal Server Error - Problem with saving the List"
        }
    return {
        'status': 200,
        'status-text': f"Added {brand}"
    }
    
def remove_brand(brand : str) -> dict:
    
    brands = file_handler.get_list()
    
    if brand in brands:
        brands.remove(brand)
        e = file_handler.write_list(brands)
        if e:
            return {
                'status': 500,
                'status-text': f"Internal Server Error - Problem with saving the List -- {e} --"
            }
        return {
            'status': 200,
            'status-text': f"Removed {brand}"
        }
        
    return {
        'status': 200,
        'status-text': f"Did Not Found {brand}"
    }

    
if __name__ == "__main__":
    main()