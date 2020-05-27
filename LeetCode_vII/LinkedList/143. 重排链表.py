## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
'''
class Solution(object):
    '''
    找到链表中间节点，将链表分成2份，翻转第二份链表，将第二份的每个节点插在第一份每个节点的后面
    时间复杂度O(N)空间复杂度O（1）
    '''''
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        if head.next is None:
            return

        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None
        second = self.reverseList(second)

        while first and second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second


    def reverseList(self, head):
        cur = head
        next = cur.next
        while next:
            head.next = next.next
            next.next = cur
            cur = next
            next = head.next
        return cur

l = make_linkedlist([1,2,3,4, 5])
Solution().reorderList(l)