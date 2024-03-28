import unittest
from src.question1 import Contracts, Contract

class TestSortContractsQuicksort(unittest.TestCase):
    def setUp(self):
        self.contracts_manager = Contracts()

    def test_sort_contracts_quicksort(self):
        """
        Testa o método test_sort_contracts_quicksort da classe Contracts.

        Verifica se o método de ordenação utilizando quicksort retorna a lista de contratos
        ordenada corretamente pelo saldo devedor em ordem decrescente.
        """
        contracts = [
            Contract(1, 100),
            Contract(2, 300),
            Contract(3, 200)
        ]

        sorted_contracts = self.contracts_manager.sort_contracts_quicksort(contracts)

        expected_contracts = [contracts[1], contracts[2], contracts[0]]
        self.assertEqual(sorted_contracts, expected_contracts)

if __name__ == '__main__':
    unittest.main()
