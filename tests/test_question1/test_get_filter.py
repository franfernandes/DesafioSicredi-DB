import unittest
from src.question1 import Contracts, Contract


class TestGetFilter(unittest.TestCase):
    def setUp(self):
        self.contracts_manager = Contracts()

    def test_get_filter(self):
        """
        Testa o método get_filter da classe Contracts.

        Verifica se o método retorna corretamente os contratos abertos que ainda não foram renegociados.
        """
        open_contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300)
        ]
        renegotiated_contracts = [1, 3]

        filtered_contracts = self.contracts_manager.get_filter(open_contracts, renegotiated_contracts)

        expected_contracts = [open_contracts[1]]
        self.assertEqual(filtered_contracts, expected_contracts)

if __name__ == '__main__':
    unittest.main()
