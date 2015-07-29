__author__ = 'Jianfeng'

"""Stack - First In Last Out (FILO).
Stack operations:
1. is_empty()
2. push()
3. pop()
"""

class Stack(object):

    def __init__(self):
        self._stack = []

    def __repr__(self):
        return str(self._stack) + ' <- Top'

    def is_empty(self):
        if self._stack:
            return False
        return True

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("stack underflow")
        top = self._stack[-1]
        del self._stack[-1]
        return top

def main():
    import random
    stack = Stack()

    for i in range(10):
        print "Before Push: ", stack
        stack.push(random.randint(0, 99))
        print "After Push: ", stack

    for i in range(11):
        print "Before Pop: ", stack
        stack.pop()
        print "After Pop: ", stack

if __name__ == '__main__':
    main()

