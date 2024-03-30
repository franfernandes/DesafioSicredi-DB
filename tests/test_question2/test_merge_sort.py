import unittest
from src.question2 import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        """
        Testa se a função merge_sort ordena corretamente a lista em ordem crescente.
        """
        arr = [5, 3, 8, 2, 7, 1, 4, 6]
        merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
