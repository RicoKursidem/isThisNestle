from os import path
import sys
sys.path.insert(0, '..')
import settings

def get_list() -> list[str]:
    """reads the txt file and converts it to a list of strings

    Returns:
        str[]: List of all lines in teh txt
    """
    with open(path.join(settings.DATA_PATH, settings.DATA_File), 'r') as f:
        lines = f.readlines()
        
        # removing al \n
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
        return lines

def write_list(items):
    """writes the given items into the data list file

    Args:
        items (list[str]): this list will overwrite the list in the data file
    """
    with open(path.join(settings.DATA_PATH, settings.DATA_File), 'w') as f:
        for line in items:
            f.write(f"{line}\n")
    
if __name__ == "__main__":
    print("This Script is not meant to be executed")