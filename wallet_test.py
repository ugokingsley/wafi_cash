import unittest
from main import WafiAccount

class WafiAccountTest(unittest.TestCase):

    def test_transfer(self):
        a = WafiAccount('a', {"USD": 10, "NGN" : 20, "GBP":10, "YUAN": 10})
        b = WafiAccount('b', {"USD": 0, "NGN" : 0, "GBP":0, "YUAN": 0})
        a.transfer("USD", 5, b)
        self.assertEqual(b.account_statement(), {"USD": 5, "NGN" : 0, "GBP":0, "YUAN": 0})
        #self.assertEqual(a.account_statement(), {"USD": 5, "NGN" : 20, "GBP":10, "YUAN": 10})


if __name__ == '__main__':
    unittest.main()
