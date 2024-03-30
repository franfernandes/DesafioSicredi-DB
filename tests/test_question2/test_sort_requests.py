import unittest
from src.question2 import sort_requests

class TestSortRequests(unittest.TestCase):
    def test_sort_requests(self):
        """
        Testa se a função sort_requests ordena corretamente a lista de requisições em ordem.
        """
        requests = [70, 30, 10]
        sort_requests(requests)
        self.assertEqual(requests, [10, 30, 70])

if __name__ == '__main__':
    unittest.main()
