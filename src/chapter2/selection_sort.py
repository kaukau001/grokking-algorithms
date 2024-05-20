class SelectionSort:
    def __init__(self, array: list):
        self.array = array

    def _search_smaller_value_index(self) -> int:
        smaller_value = self.array[0]
        smaller_index = 0
        for i in range(1, len(self.array)):
            if self.array[i] < smaller_value:
                smaller_value = self.array[i]
                smaller_index = i
        return smaller_index

    def _search_higger_value_index(self) -> int:
        higger_value = self.array[0]
        higger_index = 0
        for i in range(1, len(self.array)):
            if self.array[i] > higger_value:
                higger_value = self.array[i]
                higger_index = i
        return higger_index

    def sort_asc(self) -> list:
        sorted_array = []
        while self.array:
            smaller_value_index = self._search_smaller_value_index()
            sorted_array.append(self.array.pop(smaller_value_index))
        return sorted_array

    def sort_desc(self) -> list:
        sorted_array = []
        while self.array:
            higger_value_index = self._search_higger_value_index()
            sorted_array.append(self.array.pop(higger_value_index))
        return sorted_array
