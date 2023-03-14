import unittest
import backend

class Test_Backend(unittest.TestCase):
    
    def test_is_substring_of(self):
        self.assertTrue(backend.is_substring_of("Hello", "He"))
        self.assertTrue(backend.is_substring_of("Hello", "ello"))
        self.assertTrue(backend.is_substring_of("Hello", "lo"))
        
        self.assertTrue(backend.is_substring_of("Hello", "Hello"))
        
        self.assertFalse(backend.is_substring_of("Hello", "HelloWorld"))
        self.assertFalse(backend.is_substring_of("A", "B"))

def test():
    unittest.main()
        
if __name__ == '__main__':
    test()