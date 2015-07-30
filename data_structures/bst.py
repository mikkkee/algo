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
        return "[{v}, left: {l}, right: {r}]".format(
            v=self.value,
            l=self.left.value if self.left else None,
            r=self.right.value if self.right else None,
        )

    @property
    def depth(self):
        if self.parent is None:
            return 0
        return self.parent.depth + 1

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
        if node is None:
            node = self.root
        if node is not None:
            left = []
            right = []
            if node.left is not None:
                left = self._nodes(node.left)
            if node.right is not None:
                right = self._nodes(node.right)
            return [node] + left + right

    def find(self, key):
        """Find a node with value key."""
        node = self.root
        while node is not None:
            # Return node when found, otherwise node is None.
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

    def _successor(self, key):
        """The successor of node with value key, which should have
        two children.
        """
        node = self.find(key)
        assert(node.left and node.right)
        node = node.right
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        """Delete a node with value key."""
        node = self.find(key)
        if node is None:
            # Cannot find specified key.
            return

        if node.left is None and node.right is None:
            if node.parent is None:
                # node is root.
                self.root = None
            else:
                # node is not root.
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
        elif node.left is None:
            # node.right is not none.
            node.right.parent = node.parent
            if node.parent is None:
                # node is root.
                self.root = node.right
            else:
                # node is not root.
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
        elif node.right is None:
            # node.left is not None.
            node.left.parent = node.parent
            if node.parent is None:
                # node is root.
                self.root = node.left
            else:
                # node is not root.
                if node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
        else:
            # node has two children.
            successor = self._successor(node.value)
            # Delete successor before change node.value to avoid
            # collision.
            self.delete(successor.value)
            node.value = successor.value

def print_bst(bst):
    """A function to print ascii representation of BST."""
    max_depth = max([x.depth for x in bst._nodes()])
    max_len = max([len(str(x.value)) for x in bst._nodes()])


def main():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(-1)
    bst.insert(0)
    bst.insert(-3)
    bst.insert(1.5)
    bst.insert(2.5)
    bst.insert(3)
    bst.insert(10)
    bst.insert(8)

    print bst

    bst.delete(1)
    print bst
    print bst.root


if __name__ == '__main__':
    main()
