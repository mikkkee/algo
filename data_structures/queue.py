__author__ = 'Jianfeng'

"""Queue - First In First Out (FIFO).
Operations:
1. enqueue
2. dequeue
"""

class Queue(object):
    def __init__(self):
        self._queue = []

    def __repr__(self):
        return "Head -> " + str(self._queue)

    def is_empty(self):
        if self._queue:
            return False
        return True

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("underflow")
        head = self._queue[0]
        del self._queue[0]
        return head


def main():
    queue = Queue()
    for i in range(5):
        print "Before Insertion: ", queue
        queue.enqueue(i)
        print "After Insertion: ", queue
    for i in range(6):
        print "Before Deletion: ", queue
        queue.dequeue()
        print "After Deletion: ", queue


if __name__ == '__main__':
    main()
