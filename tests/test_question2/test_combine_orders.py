import unittest
from src.question2 import Orders

class TestCombineOrders(unittest.TestCase):
    """
    Classe de teste para a função CombineOrders
    """
    def setUp(self):
        self.orders_instance = Orders()

    def test_combine_orders(self):
        orders = [70, 30, 10]
        n_max = 100
        expected_orders = 2
        self.assertEqual(self.orders_instance.combine_orders(orders, n_max), expected_orders)

       # Caso de teste adicional
        orders = [50, 60, 40, 30, 20, 10]
        n_max = 100
        expected_orders = 3
        self.assertEqual(self.orders_instance.combine_orders(orders, n_max), expected_orders)

        # Caso de teste com apenas uma requisição
        orders = [90]
        n_max = 100
        expected_orders = 1
        self.assertEqual(self.orders_instance.combine_orders(orders, n_max), expected_orders)

        # Caso de teste em que existem requisições repetidas.
        orders = [200, 100, 200, 100, 200, 100]
        n_max = 300
        expected_orders = 3
        self.assertEqual(self.orders_instance.combine_orders(orders, n_max), expected_orders)

if __name__ == '__main__':
    unittest.main()
