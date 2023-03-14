import unittest

import sys
sys.path.insert(0, '..')
import settings
settings.DATA_PATH = "./backend/data"
settings.DATA_File = "list_test.txt"

from backend import file_handler

class Test_File_Handler(unittest.TestCase):
    
    def test_get_list(self):
        file_handler.write_list(["Apfel","Birne","Banane"])
        self.assertEqual(file_handler.get_list(), ["Apfel","Birne","Banane"])
    
    def test_write_list(self):
        file_handler.write_list(["Apfel","Birne","Banane"])
        
        self.assertEqual(file_handler.get_list(), ["Apfel","Birne","Banane"])
        
        file_handler.write_list(["Apfel","Banane","Birne", "Traube"])
        self.assertEqual(file_handler.get_list(), ["Apfel","Banane","Birne", "Traube"])
        
        file_handler.write_list(["Apfel","Birne","Banane"])
        self.assertEqual(file_handler.get_list(), ["Apfel","Birne","Banane"])

def test():
    unittest.main()
        
if __name__ == '__main__':
    test()
    