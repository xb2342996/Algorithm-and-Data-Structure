## written by xiongbiao
## date 2020-5-25

'''
给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素，使这个列表仍然是循环升序的。给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个点。否则。请返回原先给定的节点。
'''

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(object):
    '''
    顺序循环链表插入，无论如何都要循环一遍链表，循环跳出条件为head=prev，如果prev的值小于insertVal小于cur的值，插入节点结束
    如果pre的值大于cur的值并且insertVal大于pre或者insertVal小于cur，插入节点结束
    跳出循环说明insertVal插在prev的后面cur的前面
    '''
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal, None)
        if head is None:
            new_node.next = new_node
            return new_node

        if head == head.next:
            head.next = new_node
            new_node.next = head
            return new_node

        prev, cur = head, head.next
        flag = False
        while True:

            if prev.val <= insertVal <= cur.next.val:
                flag = True
            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    flag =True

            if flag:
                prev.next = Node(insertVal, cur)
                return head
            prev, cur = cur, cur.next
            if prev == head:
                break

        prev.next = Node(insertVal, cur)
        return head




