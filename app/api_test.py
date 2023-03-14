import unittest

import api

class Test_Api(unittest.TestCase):
    
    def test_get_list(self):
        self.assertIn("A", ["A"], "msg")

def test():
    unittest.main()
        
if __name__ == '__main__':
    test()
    