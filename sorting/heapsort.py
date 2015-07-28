__author__ = 'Jianfeng'

"""This is a max heap"""

def heapify(a, i, heap_size):
    # heapify(a, i) assumes that the sub heap rooted at
    # left(i) and right(i) are already heapified.
    # Remember to heapify left/right if a smaller value is
    # swapped to left/right position.
    # Heap_size has to be explicitly passed because it may
    # not equal to len(a).
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and a[left] > a[i]:
        largest = left
    else:
        largest = i

    if right < heap_size and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest, heap_size)

def build_heap(a):
    heap_size = len(a)
    heap_body = (heap_size - 2) / 2
    for i in range(heap_body, -1, -1):
        heapify(a, i, heap_size)

def heapsort(a):
    build_heap(a)

    heap_size = len(a)
    last_index = heap_size - 1

    while last_index > 0:
        a[0], a[last_index] = a[last_index], a[0]
        heap_size -= 1
        last_index -= 1
        heapify(a, 0, heap_size)

def main():
    import random

    a = random.sample(range(100), 10)
    print "Unsorted: ", a
    build_heap(a)
    print "Heapified: ", a
    heapsort(a)
    print "Sorted: ", a

if __name__ == '__main__':
    main()
