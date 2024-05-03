def binary_search(ordered_list: list, item: int):
    low = 0
    high = len(ordered_list) - 1
    while low <= high:
        middle = (high + low) // 2
        k = ordered_list[middle]
        if k == item:
            return middle
        if k > item:
            high = middle - 1
        else:
            low = middle + 1
    return None


