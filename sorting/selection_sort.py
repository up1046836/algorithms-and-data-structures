def selection_sort(lst):
    for i in range(len(lst)):
        min_value = float('inf')
        min_index = None
        for j in range(i, len(lst)):
            if lst[j] < min_value:
                min_value = lst[j]
                min_index = j
        tmp = lst[i]
        lst[i] = min_value
        lst[min_index] = tmp
        
    return lst
