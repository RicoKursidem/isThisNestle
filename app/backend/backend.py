import file_handler as file_handler

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
    return substring.lower() in string.lower()

def get_brands(text: str):
    
    brands = file_handler.get_list()
    ret_Brands = []
    
    for brand in brands:
        if is_substring_of(brand, text):
            ret_Brands.append(brand)
    
    return ret_Brands



if __name__ == "__main__":
    main()