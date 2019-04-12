import unittest

class UtilsTest(unittest.TestCase):

    def setUp(self):
        path = "data"

    def test_list_files(self):
        value = 6
        self.assertEqual(value, 6)

if __name__ == '__main__':
    unittest.main()      