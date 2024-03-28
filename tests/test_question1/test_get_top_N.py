import unittest
from src.question1 import Contracts, Contract

class TestGetTopN(unittest.TestCase):
    def setUp(self):
        self.contracts_manager = Contracts()

    def test_get_top_N(self):
        """
        Testa o método get_top_N da classe Contracts.
        Verifica se o método retorna os N principais devedores corretamente.
        """
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        top_n = 2

        top_debtors = self.contracts_manager.get_top_N(contracts, top_n)

        expected_debtors = [3, 2]
        self.assertEqual(top_debtors, expected_debtors)

if __name__ == '__main__':
    unittest.main()
