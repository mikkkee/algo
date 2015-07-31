__author__ = 'Jianfeng'
"""Knapsack problem
Given a set of items, each with weight w[i] and value v[i], choose
from the set of items to maximize the total value while restrict total
weight no larger than W.
"""

def knapsack(weight, value, W):
    prev = [0 for x in range(W+1)]
    curr = [0 for x in range(W+1)]
    n = len(weight)
    assert(n == len(value))

    for i in range(n):
        for w in range(W+1):
            if w - weight[i] >= 0:
                if prev[w - weight[i]] + value[i] > curr[w]:
                    curr[w] = prev[w - weight[i]] + value[i]
        prev = [x for x in curr]

    return curr


def main():
    import random
    weight = random.sample(range(15), 5)
    value = random.sample(range(20), 5)
    W = random.randint(0, 50)

    print "Weight: ", str(weight)
    print "Value: ", str(value)
    print "W: ", W

    opt = knapsack(weight, value, W)
    print "Opt: ", opt

if __name__ == '__main__':
    main()


