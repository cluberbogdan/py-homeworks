import unittest
from io import StringIO
import sys
from contextlib import contextmanager
from lesson14 import Bank, CurrentAccount

@contextmanager
def mock_stdout():
    # Redirect stdout to capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output

    try:
        yield captured_output
    finally:
        # Reset stdout
        sys.stdout = sys.__stdout__

class TestSendOverdraftLetter(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_send_overdraft_letter(self):
        current_account = CurrentAccount(-500.0, "CA456", -100.0)
        self.bank.open_account(current_account)

        with mock_stdout() as stream:
            self.bank.update()
            self.assertIn("Overdraft letter sent for account number CA456", stream.getvalue())
        
if __name__ == '__main__':
    unittest.main()
