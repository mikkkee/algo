__author__ = 'Jianfeng'

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

def list_search(head, k):
    item = head
    while item.next:
        if item.next.val == k:
            return item
        else:
            item = item.next
    return None

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next
