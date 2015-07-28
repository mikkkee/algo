__author__ = 'Jianfeng'

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

def main():
    import random

    a = random.sample(range(100), 10)
    print "Unsorted a: ", a
    insertion_sort(a)
    print "Sorted a: ", a


if __name__ == '__main__':
    main()
