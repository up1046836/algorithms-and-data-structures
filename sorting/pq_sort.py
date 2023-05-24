from importlib import import_module

pq = import_module(".pq", package="data-structures")
heap = import_module(".heap", package="data-structures")

PriorityQueue1 = pq.PriorityQueue1
Heap = heap.Heap

class PQSort:
    def sort(lst, pq):
        pq = pq()
        while lst: pq.insert(lst.pop())
        while pq.size(): lst.append(pq.remove())
        return lst

class InsertionSort(PQSort):
    def sort(lst):
        return PQSort.sort(lst, PriorityQueue1) 

pq_insertion_sort = InsertionSort.sort
