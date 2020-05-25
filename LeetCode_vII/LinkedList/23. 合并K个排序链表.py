## written by xiongbiao
## date 2020-5-25

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

class Solution(object):
    '''
    重写ListNode的比较方法__gt__, __lt__, __eq__方法，讲每个链表头结点放入队列，弹出队列中最小的元素，将弹出的链表节点的下一个节点放入队列
    拼接弹出的没一个节点。时间复杂度O（KNlogN), 空间复杂度O（K）
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        from queue import PriorityQueue
        pq = PriorityQueue()
        for node in lists:
            pq.put(node)

        dummy = ListNode(0)
        cur = dummy
        while not pq.empty():
            node = pq.get()
            if node.next:
                pq.put(node.next)
            cur.next = node
            cur = cur.next

        return dummy.next

    '''
    优化思路：
    K个链表，可分治思路优化合并操作，时间复杂度O（KNlogK），空间复杂度O（N）
    '''
    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     return self.mergeLists(0, len(lists) - 1, lists)
    #
    # def mergeLists(self, left, right, lists):
    #     if left == right:
    #         return lists[left]
    #     if left > right:
    #         return None
    #     mid = (left + right) >> 1
    #     left_list = self.mergeLists(left, mid, lists)
    #     right_list = self.mergeLists(mid + 1, right, lists)
    #     return self.mergeTwo(left_list, right_list)
    #
    # def mergeTwo(self, node_1, node_2):
    #     if node_1 is None:
    #         return node_2
    #     if node_2 is None:
    #         return node_1
    #
    #     if node_1.val < node_2.val:
    #         head = node_1
    #         node_1 = node_1.next
    #     else:
    #         head = node_2
    #         node_2 = node_2.next
    #
    #     node = head
    #     while node_1 and node_2:
    #         if node_1.val < node_2.val:
    #             node.next = node_1
    #             node_1 = node_1.next
    #         else:
    #             node.next = node_2
    #             node_2 = node_2.next
    #         node = node.next
    #
    #     if node_1:
    #         node.next = node_1
    #     if node_2:
    #         node.next = node_2
    #
    #     return head

    '''
    拼接K个链表
    解题思路：
    顺序拼接每个链表，变成子问题位拼接2个链表的问题，时间复杂度O（KKN）， 空间复杂度O（1），
    '''
    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     if lists is None:
    #         return None
    #     if len(lists) == 0:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #
    #     merged = None
    #     for n in lists:
    #         merged = self.mergeTwo(n, merged)
    #     show_linkedlist(merged)
    #     return merged
    #
    #

l1 = [1, 4, 5]
l2 = [1, 3, 4]
l3 = [2, 6]
n1 = make_linkedlist(l3)
n2 = make_linkedlist(l2)
n3 = make_linkedlist(l1)
Solution().mergeKLists([n1, n2, n3])