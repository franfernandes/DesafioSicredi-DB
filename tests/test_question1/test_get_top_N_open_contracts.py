import unittest
from src.question1 import Contracts, Contract

class TestGetTopNOpenContracts(unittest.TestCase):
    def setUp(self):
        self.contracts_manager = Contracts()

    def test_get_top_N_open_contracts(self):
        """
        Testa o método get_top_N_open_contracts da classe Contracts.

        Verifica se o método retorna os N principais contratos abertos corretamente,
        considerando contratos não renegociados.
        """
        open_contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        renegotiated_contracts = [1]
        top_n = 2

        top_open_contracts = self.contracts_manager.get_top_N_open_contracts(open_contracts, renegotiated_contracts, top_n)

        expected_open_contracts = [3, 2]
        self.assertEqual(top_open_contracts, expected_open_contracts)

if __name__ == '__main__':
    unittest.main()

