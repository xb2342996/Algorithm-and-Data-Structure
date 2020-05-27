## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个链表（链表结点包含一个整型值）的头结点 head。
同时给定列表 G，该列表是上述链表中整型值的一个子集。
返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。
'''
class Solution(object):
    '''
    将G变为set确保元素唯一性，寻找每个组件的最后一位，直到最后一个节点的前一个节点为止，最后处理最后一个节点
    '''
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        count = 0
        node = head
        while node.next:
            if node.val in g and node.next.val not in g:
                count += 1
            node = node.next

        if node.val in g:
            count += 1

        return count
