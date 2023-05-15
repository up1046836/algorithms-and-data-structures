def binary_search(lst, value):
    def inner(lst, value, left, right):
        middle = (left + right) // 2
        current = lst[middle]

        if current == value:
            return middle
        elif left == right:
            return None 
        elif current > value:
            return inner(lst, value, left, middle - 1)
        elif current < value:
            return inner(lst, value, middle + 1, right)

    left = 0
    right = len(lst) - 1
    return inner(lst, value, left, right)


