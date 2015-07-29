__author__ = 'Jianfeng'

"""Radix sort uses a stable sorting algorithm."""

def counting_for_radix(a, index, k=9):
    # A special counting sort for radix sort that uses one digit at
    # specified position index as the sorting key.
    c = [0 for x in range(k+1)]
    b = [0 for x in range(len(a))]

    for x in a:
        c[int(x[index])] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]

    for i in range(len(a)-1, -1, -1):
        x = a[i]
        b[c[int(x[index])]-1] = x
        c[int(x[index])] -= 1
    return b

def radix_sort(a, k):
    """Sort elements in a.
    Elements in a are str(numbers) with maximum k digits."""
    for i in range(k-1, -1, -1):
        a = counting_for_radix(a, i)
    return a

def main():
    import random
    a = random.sample(range(1000), 20)
    a = ["{i:03d}".format(i=x) for x in a]
    print "Unsorted: ", a
    a = radix_sort(a, 3)
    print "Sorted: ", a


if __name__ == '__main__':
    main()
