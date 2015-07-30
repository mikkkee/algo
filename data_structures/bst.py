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

    def __repr__(self):
        return "Value: {v}, left: {l}, right: {r}".format(
            v=self.value,
            l=self.left.value if self.left else None,
            r=self.right.value if self.right else None
        )

class BST(object):
    def __init__(self, key=None):
        if key is not None:
            node = Node(key)
            self.root = node
        else:
            self.root = None

    def __repr__(self):
        return str(self._nodes())

    def _nodes(self, node=None):
        """All current nodes of bst."""

    def find(self, key):
        """Find a node with value key."""
        node = self.root
        while node is not None:
            if key == node.value:
                return node
            elif key > node.value:
                node = node.right
            else:
                node = node.left
        return node

    def insert(self, key):
        """Insert a node with value key into BST."""
        item = self.root
        prev = item
        while item is not None:
            prev = item
            if key > item.value:
                item = item.right
            else:
                item = item.left
        new_node = Node(key)
        if prev is not None:
            new_node.parent = prev
            if new_node.value > prev.value:
                prev.right = new_node
            else:
                prev.left = new_node
        else:
            self.root = new_node


def main():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(-1)
    print bst.root
    print bst


if __name__ == '__main__':
    main()
