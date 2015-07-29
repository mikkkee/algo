__author__ = 'Jianfeng'
import random

def partition(a, left, right):
    # Divide a list a into two parts by using a index pivot.
    # All items to the left of pivot are less than a[pivot]
    # All items to the right of pivot are >= to a[pivot]
    j = left
    i = left
    p = random.randint(left, right - 1)
    a[p], a[right-1] = a[right-1], a[p]
    pivot = right - 1
    while j < pivot:
        if a[j] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        else:
            j += 1
    a[i], a[pivot] = a[pivot], a[i]
    return i

def quicksort(a, left, right):
    if right - left > 1:
        pivot = partition(a, left, right)
        quicksort(a, left, pivot)
        quicksort(a, pivot, right)

def main():
    import random

    a = random.sample(range(100), 10)
    print "Unsorted: ", a
    quicksort(a, 0, len(a))
    print "Sorted: ", a

if __name__ == '__main__':
    main()
