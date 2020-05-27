## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
对链表进行插入排序
'''
class Solution(object):
    '''
    拿到一个节点将节点拼入新的链表
    时间复杂度O（N）空间复杂度O（1）
    '''
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(-0)
        cur = dummy
        node = head
        while node:
            if cur.next is None or cur.next.val > node.val:
                prev = node.next
                node.next = cur.next
                cur.next = node
                cur = dummy
                node = prev
            else:
                cur = cur.next

        return dummy.next

l = make_linkedlist([-1,5,3,4,0])
show_linkedlist(Solution().insertionSortList(l))
