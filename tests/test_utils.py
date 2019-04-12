from src.utils import utils
import os
import unittest

class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.path = (os.path.dirname(__file__) + "\data")

    def test_list_files(self):
        value = utils.listfiles(self.path)
        self.assertEqual(len(value), 2)

if __name__ == '__main__':
    unittest.main()      