def insert(lst, j):
    elem = lst[j]
    i = j - 1
    while i >= 0 and lst[i] > elem:
        lst[i + 1] = lst[i]
        i -= 1

    lst[i + 1] = elem

def recursive_insertion_sort(lst, j):
    if j > 0:
        recursive_insertion_sort(lst, j-1)
        insert(lst, j)
    return lst
