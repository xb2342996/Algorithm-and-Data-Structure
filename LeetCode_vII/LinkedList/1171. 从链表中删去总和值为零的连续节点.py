## written by xiongbiao
## date 2020-5-26
from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。
'''

class Solution(object):
    '''
    前缀数组和，第一次扫描获取最后一次出现这个sum和的位置，第二次扫描若当前节点处sum在下一处出现了则表明两结点之间所有节点和为0 直接删除区间所有节点
    时间复杂度O(N）空间复杂度O(1)
    '''
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        diff = {}
        sum = 0
        node = dummy
        while node:
            sum += node.val
            diff[sum] = node
            node = node.next

        sum = 0
        node = dummy
        while node:
            sum += node.val
            node.next = diff[sum].next
            node = node.next

        return dummy.next

l = make_linkedlist([1, 2, 3, -3, -2])
show_linkedlist(Solution().removeZeroSumSublists(l))