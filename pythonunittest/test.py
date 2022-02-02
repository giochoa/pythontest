import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('test function')
    def test_stuff(self):
        test_num = 144
        result = main.stuff(test_num)
        self.assertEqual(result, 149)


    def test_stuff2(self):
        test_num = 'testtest'
        result = main.stuff(test_num)
        self.assertIsInstance(result, ValueError) 

    def test_stuff3(self):
        test_num = None
        result = main.stuff(test_num)
        self.assertEqual(result, 'Please a number here')

    def test_stuff4(self):
        test_num = ''
        result = main.stuff(test_num)
        self.assertEqual(result, 'Please a number here') 

    def tearDown(s):
        print('cleaning up')       


if __name__ == '__main__':
    unittest.main()