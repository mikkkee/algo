__author__ = 'Jianfeng'

def merge_sort(a, left, right):
    # The left and right indexes here are normal Python list indexes.
    # i.e. left is inclusive while right is not.
    if left < right - 1:
        # Only sort when list length (right - left) is larger than 1.
        pivot = (right + left) / 2
        merge_sort(a, left, pivot)
        merge_sort(a, pivot, right)
        merge(a, left, pivot, right)

def merge(a, left, pivot, right):
    inf = float('infinity')
    L = a[left:pivot]
    R = a[pivot:right]
    L.append(inf)
    R.append(inf)
    il = 0
    ir = 0

    for i in range(left, right):
        if L[il] < R[ir]:
            a[i] = L[il]
            il += 1
        else:
            a[i] = R[ir]
            ir += 1

def main():
    import random

    a = random.sample(range(100), 11)
    print "Unsorted a: ", a
    merge_sort(a, 0, len(a))
    print "Sorted a: ", a


if __name__ == '__main__':
    main()
