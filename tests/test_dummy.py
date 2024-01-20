import unittest
from src.model_dummy import returnTrue


class DummyTest(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(returnTrue())
