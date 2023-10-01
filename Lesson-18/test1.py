import unittest
from lesson14 import Bank, SavingsAccount

class TestBank(unittest.TestCase):

    def test_open_account(self):
        bank = Bank()

        test_account = SavingsAccount(1000.0, 'SA001', 0.03)

        bank.open_account(test_account)

        self.assertIn(test_account, bank.accounts)

        self.assertEqual(test_account.get_balance(), 1000.0)

if __name__ == '__main__':
    unittest.main()