import unittest

class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status
    
    def __repr__(self):
        return f"Transaction({self.number}, {self.funds}, {self.status})"
    
    def __str__(self):
        return f"Transaction({self.number}, {self.funds}, {self.status})"

class TestTransaction(unittest.TestCase):
    
    def test_initialization(self):
        t = Transaction("TX001", 1000.0)
        self.assertEqual(t.number, "TX001")
        self.assertEqual(t.funds, 1000.0)
        self.assertEqual(t.status, "active")

    def test_str_output(self):
        t = Transaction("TX002", 500, "pending")
        expected = "Transaction(TX002, 500, pending)"
        self.assertEqual(str(t), expected)

    def test_repr_output(self):
        t = Transaction("TX003", 750.5, "completed")
        expected = "Transaction(TX003, 750.5, completed)"
        self.assertEqual(repr(t), expected)

if __name__ == "__main__":
    unittest.main()
