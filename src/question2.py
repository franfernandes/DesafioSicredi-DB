def merge_sort(arr):
    """
    Algoritmo de ordenação Merge Sort
    :arr(list): Lista a ser ordenada.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def sort_requests(requests):
    """
    Ordena a lista de requisições em ordem decrescente.
    :requests (list): Lista de inteiros representando as requisições.
    """
    merge_sort(requests)

class Orders:
    def combine_orders(self, requests, n_max):
        """
        Calcula o número mínimo de viagens necessário para atender todas as requisições.

        :requests(list[int]): Uma lista de valores requisitados pelas agências.
        :n_max(int): O valor monetário máximo que pode ser transportado em uma única viagem.
        :return(int): O número mínimo de viagens necessário para atender todas as requisições.
        """
        merge_sort(requests)

        total_trips = 0

        while len(requests) > 0:
            
            if len(requests) <= 2 and sum(requests) <= n_max:
                total_trips += 1
                break
            
            first_request = requests[0]
            last_request = requests[-1]
    
            if first_request + last_request <= n_max:
                requests.pop(0)
                requests.pop()
                total_trips += 1
    
            else:
                requests.pop(0)
                requests.pop()
                if requests:
                    requests.pop(0)
                if requests:
                    requests.pop()
                total_trips += 2
    
        return total_trips
