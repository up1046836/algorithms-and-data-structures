# p, q and r are indexes (start, middle, end)
def merge(lst, p, q, r):
    left = lst[p:q+1]
    right = lst[q+1:r+1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1

def merge_sort(lst, p, r):
    q = (p + r)//2
    if p < r:
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)
    return lst
