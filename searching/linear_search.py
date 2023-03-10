def linear_search(lst, value):
    i = None
    for j in range(len(lst)):
        if lst[j] == value:
            i = j
    return i
