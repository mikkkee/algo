__author__ = 'Jianfeng'

"""BST operations:
1. find
2. insert
3. delete
4. predecessor
5. successor
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST(object):
    def __init__(self, node):
        assert(isinstance(node, Node))
        self.root = node
        self.node.parent = None

    def find(self, key):
        """Find a node with value key."""
        pass
