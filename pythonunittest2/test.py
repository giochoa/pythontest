import unittest
import script

class TestGame(unittest.TestCase):
    def testinput(self):
        guess = 5
        answer = 5
        result = script.guess_game(guess, answer)
        self.assertTrue(result)
    
    def testinputwronginput(self):
        guess = 5
        answer = 0
        result = script.guess_game(guess, answer)
        self.assertFalse(result)
    
    def testinputwronginput3(self):
        guess = 5
        answer = 11
        result = script.guess_game(guess, answer)
        self.assertFalse(result)        



if __name__ == '__main__':
    unittest.main()

