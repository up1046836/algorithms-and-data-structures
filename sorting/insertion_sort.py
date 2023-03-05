def insertion_sort(lst):
    for j in range(1, len(lst)):
        elem = lst[j]
        i = j - 1
        while i >= 0 and lst[i] > elem:
            lst[i + 1] = lst[i]
            i = i - 1

        lst[i + 1] = elem
    return lst
