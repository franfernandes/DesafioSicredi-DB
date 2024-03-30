import unittest
from src.question1 import Contracts, Contract

class TestGetTopN(unittest.TestCase):
    def setUp(self):
        self.contracts_manager = Contracts()

    def test_get_top_N(self):
        """
        Testa o método get_top_N da classe Contracts.
        Verifica se o método retorna os N devedores da lista .
        """
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300),
            Contract(4, 400)
        ]
        top_n = 3

        top_debtors = self.contracts_manager.get_top_N(contracts, top_n)

        expected_debtors = [1, 2, 3]  # Contratos ordenados por id
        self.assertEqual(top_debtors, expected_debtors)


if __name__ == '__main__':
    unittest.main()
