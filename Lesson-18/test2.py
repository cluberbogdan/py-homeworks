import unittest
from io import StringIO
import sys
from lesson14 import Bank, CurrentAccount

class TestSendOverdraftLetter(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_send_overdraft_letter(self):
        current_account = CurrentAccount(-500.0, "CA456", -100.0)
        self.bank.open_account(current_account)

        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.bank.update()

        # Reset stdout
        sys.stdout = sys.__stdout__

        self.assertIn("Overdraft letter sent for account number CA456", captured_output.getvalue())
        
if __name__ == '__main__':
    unittest.main()
