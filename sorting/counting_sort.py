__author__ = 'Jianfeng'
"""
Counting sort assumes that each of the n input elements is an integer
in the range 0 to k.
Counting sort needs two additional lists besides the input list A[1..n],
B[1..n], which holds the sorted output, and C[0..k], which provides
temporary working storage.
Counting sort is a stable sort, which preserves the order for elements
of the same value as the order in input list.
"""

def counting_sort(a, k):
    c = [0 for x in range(k+1)]
    b = [0 for x in range(len(a))]
    for x in a:
        c[x] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for i in range(len(a)-1, -1, -1):
        # Go from tail to head to preserve same order for ties as
        # that in input list. i.e. stable.
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b

def main():
    import random
    k = 50
    n = 100
    assert(n > k)
    a = [random.choice(xrange(0, k)) for x in xrange(n)]
    print "Unsorted: ", a
    b = counting_sort(a, k)
    print "Sorted: ", b

if __name__ == '__main__':
    main()