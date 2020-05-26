## written by xiongbiao
## date 2020-5-26

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
'''

class Solution(object):
    '''
    用快慢指针找到相交的点，此时快指针走了a+nb（a为从头结点进入环的长度，b为环的长度）此时慢指针走了nb
    将快指针放在head节点，快慢指针一起移动，相交的点就是环的入口。
    时间复杂度O（N） 空间复杂度O（1）
    '''
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
