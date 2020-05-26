## written by xiongbiao
## date 2020-5-26
from LinkedList.node import Node

'''
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中
'''

class Solution(object):
    '''
    创建虚拟头结点，遍历链表，如果节点有next将next压栈，如果节点有child将child压栈，每次弹出一个节点，拼接，将child变为None
    '''
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        dummy = Node(0, None, head, None)
        cur = dummy
        stack = []
        stack.append(head)
        while len(stack) > 0:
            node = stack.pop()

            cur.next = node
            node.prev = cur
            cur = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
        head = dummy.next
        head.prev = None
        return head


    '''
    创建虚拟头结点dummy，递归深度优先遍历链表的child链，进入child链之前保存有child节点的下一个节点，将child内的每个node拼接到dummy上，将每个拼接到dummy上的节点的child置为null
    时间复杂度O(N)，空间复杂度O(N)
    '''
    # def flatten(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """
    #     if head is None:
    #         return None
    #     dummy = Node(0, None, head, None)
    #     self.append(head, dummy)
    #     head = dummy.next
    #     head.prev = None
    #     return head
    #
    # def append(self, cur, dummy):
    #     while cur:
    #         dummy.next = cur
    #         cur.prev = dummy
    #         dummy = dummy.next
    #         if cur.child:
    #             next = cur.next
    #             dummy = self.append(cur.child, dummy)
    #             cur.child = None
    #             cur = next
    #         else:
    #             cur = cur.next
    #
    #     return dummy
#
n1 = Node(1, None, None, None)
n2 = Node(2, n1, None, None)
n3 = Node(3, n2, None, None)
n4 = Node(4, n3, None, None)
n5 = Node(5, n4, None, None)
n6 = Node(6, n5, None, None)
n7 = Node(7, n6, None, None)
n8 = Node(8, n7, None, None)
n9 = Node(9, n8, None, None)
n10 = Node(10, n9, None, None)
n11 = Node(11, n10, None, None)
n12 = Node(12, n11, None, None)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n7.next = n8
n8.next = n9
n9.next = n10

n11.next = n12

n3.child = n7
n8.child = n11

head = Solution().flatten(n1)

