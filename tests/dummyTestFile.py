import unittest
from dummyFile import returnTrue

class DummyTest(unittest.TestCase):
    
    def test_dummy(self):
        self.assertTrue(returnTrue())