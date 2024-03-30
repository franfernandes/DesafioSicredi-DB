class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:

    def get_filter(self, open_contracts, renegotiated_contracts):
        """
        Filtra os contratos abertos que ainda não foram renegociados.

        :open_contracts(list[Contract]): Lista de contratos abertos.
        :renegotiated_contracts(list[int]): Lista de identificadores dos contratos renegociados.
        :return(list[Contract]): Lista de contratos abertos e não renegociados.

        """
        return [contract for contract in open_contracts if contract.id not in renegotiated_contracts]
    
    def sort_contracts_quicksort(self, contracts):
        """
        Ordena os contratos pelo saldo devedor em ordem decrescente usando o algoritmo quicksort.

        :contracts(list[Contract]): Lista de contratos.
        :return(list[Contract]): Lista de contratos ordenados pelo saldo devedor em ordem decrescente.
        """
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2].debt
            left = [x for x in arr if x.debt > pivot]
            middle = [x for x in arr if x.debt == pivot]
            right = [x for x in arr if x.debt < pivot]
            return quicksort(left) + middle + quicksort(right)
        
        return quicksort(contracts)
    def get_top_N(self, contracts, top_n):
        """
        Retorna os N principais devedores.

        :contracts(list[Contract]): Lista de contratos.
        :top_n(int): Número de principais devedores a serem retornados.
        :return(list[int]): Lista de identificadores dos N principais devedores.
        """
        return [contract.id for contract in contracts[:top_n]]
    
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Retorna uma lista de identificadores dos N principais devedores que não renegociaram suas dívidas.

        :open_contracts(list[Contract]): Uma lista de contratos abertos.
        :renegotiated_contracts(list[int]): Uma lista de identificadores dos contratos renegociados.
        :top_n(int): O número de principais devedores a serem retornados.
        :return(list[int]): Uma lista contendo os identificadores dos N principais devedores em ordem decrescente.
        """
        contracts_open = self.get_filter(open_contracts, renegotiated_contracts)
        sorted_contracts = self.sort_contracts_quicksort(contracts_open)
        top_n_debtors = self.get_top_N(sorted_contracts, top_n)
        return top_n_debtors
