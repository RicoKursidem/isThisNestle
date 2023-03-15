import unittest

import sys
sys.path.insert(0, '..')
import settings
settings.DATA_PATH = "./backend/data"

from backend import file_handler, backend_api

class Test_Backend(unittest.TestCase):
    
    def test_is_substring_of(self):
        self.assertTrue(backend_api.is_substring_of("Hello", "He"))
        self.assertTrue(backend_api.is_substring_of("Hello", "ello"))
        self.assertTrue(backend_api.is_substring_of("Hello", "lo"))
        self.assertTrue(backend_api.is_substring_of("Hello", ""))
        
        self.assertTrue(backend_api.is_substring_of("Hello", "Hello"))
        
        self.assertFalse(backend_api.is_substring_of("Hello", "HelloWorld"))
        self.assertFalse(backend_api.is_substring_of("A", "B"))
        
        self.assertTrue(backend_api.is_substring_of("Nestlé", "e"))
        self.assertTrue(backend_api.is_substring_of("L'Oreal", "L Oreal"))
    
    def test_get_brands(self):
        file_handler.write_list(['Apple', 'App', 'Fruity'])
        
        self.assertTrue(is_in_array(['App', 'Apple'], backend_api.get_brands('Ap')))
        self.assertTrue(is_in_array(['Apple'], backend_api.get_brands('Appl')))
        self.assertTrue(is_in_array(['Apple', 'App', 'Fruity'], backend_api.get_brands('')))
        self.assertTrue(is_in_array(['Fruity'], backend_api.get_brands('Fruity')))
        
        
        
def is_in_array(items, array):
        for item in items:
            if not item in array:
                return False
        return True
        

def test():
    unittest.main()
        
if __name__ == '__main__':
    test()