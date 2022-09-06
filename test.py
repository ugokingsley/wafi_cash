import unittest
from main import WafiAccount

class WafiAccountTest(unittest.TestCase):
    def test_deposit(self):
        a = WafiAccount('a', 0)
        a.deposit(10)
        self.assertEqual(a.account_statement(), 10)

    def test_withdraw(self):
        b = WafiAccount('a', 100)
        b.withdraw(10)
        self.assertEqual(b.account_statement(), 90)

    def test_transfer(self):
        a = WafiAccount('a', 0)
        b = WafiAccount('b', 0)
        b.deposit(100)
        b.transfer(15, a)
        self.assertEqual(b.account_statement(), 85)
        self.assertEqual(a.account_statement(), 15)


if __name__ == '__main__':
    unittest.main()
