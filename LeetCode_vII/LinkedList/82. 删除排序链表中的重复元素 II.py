## written by xiongbiao
## date 2020-5-26
from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
'''
class Solution(object):

    '''
    创建虚拟头结点，prev指向虚拟头结点，cur指向head，遍历链表，如果cur的next=cur，获取重复元素的区间的左节点prev，找到从cur开始第一个值不等于cur的点
    将prev与得到的不相等的点拼上
    时间复杂度O(N) 空间复杂度O(1)
    '''
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head

        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = self.findSame(prev, cur.val)
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next

    def findSame(self, prev, val):

        node = prev.next
        while node and node.val == val:
            node = node.next
        prev.next = node
        return node
    '''
    2次遍历列表，第一次存储每个元素出现的次数，第二次遍历删除索引大于2的元素
    时间复杂度O(N) 空间复杂度O(N)
    '''
    # def deleteDuplicates(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None or head.next is None:
    #         return head
    #
    #     node = head
    #     total = {}
    #     while node:
    #         if node.val not in total:
    #             total[node.val] = 1
    #         else:
    #             total[node.val] += 1
    #         node = node.next
    #
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     prev, cur = dummy, head
    #
    #     while cur:
    #         if total[cur.val] > 1:
    #             prev.next = cur.next
    #             cur = prev.next
    #         else:
    #             prev = prev.next
    #             cur = cur.next
    #
    #     return dummy.next

l = make_linkedlist([1,2,2,3,3,4,4,5,5,5,6])
show_linkedlist(Solution().deleteDuplicates(l))


