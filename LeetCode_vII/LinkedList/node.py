# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def make_linkedlist(lists):
    if lists is None or len(lists) == 0:
        return None

    head = ListNode(lists[0])
    node = head
    for i in range(1, len(lists)):
        node.next = ListNode(lists[i])
        node = node.next
    return head

def show_linkedlist(head):
    if head is None:
        print(None)
        return

    s = str(head.val)
    node = head.next
    while node:
        s += ' -> ' + str(node.val)
        node = node.next
    print(s)