## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。
'''

class Solution(object):

    '''
    虚拟头结点，创建一个小于x的头结点和一个大于等于x的头结点，将小于x的节点拼在小的头结点上，大于x的拼在大的头结点上，拼接大小节点，返回小虚拟头结点的下一个节点
    时间复杂度O（N）空间复杂度O（1）
    '''
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        large = ListNode(0)
        l_node = large
        small = ListNode(0)
        s_node = small
        node = head
        while node:
            if node.val < x:
                s_node.next = node
                s_node = s_node.next
            else:
                l_node.next = node
                l_node = l_node.next
            node = node.next
        l_node.next = None
        s_node.next = large.next
        return small.next

l = make_linkedlist([1,4,3,2,5,2])
show_linkedlist(Solution().partition(l, 3))