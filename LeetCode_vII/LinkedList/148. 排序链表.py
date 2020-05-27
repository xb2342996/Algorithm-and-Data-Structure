## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
'''
class Solution(object):
    '''
    自顶向下每次拿2倍的元素去排序，排序后将链表接在原先的链表上
    时间复杂度O（nlogn) 空间复杂度O（1）
    '''
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        length = 0
        while node:
            node = node.next
            length += 1
        if length == 0: return

        dummy = ListNode(0)
        dummy.next = head
        interval = 1

        while interval < length:
            prev = dummy
            cur = prev.next
            while cur:
                first = cur
                for j in range(interval - 1):
                    if cur:
                        cur = cur.next
                if cur is None:
                    break

                second = cur.next
                cur.next = None
                cur = second
                for j in range(interval - 1):
                    if cur:
                        cur = cur.next
                rest = None
                if cur:
                    rest = cur.next
                    cur.next = None

                cur = rest
                prev.next = self.merge(first, second)
                while prev.next:
                    prev = prev.next
                prev.next = rest
            interval *= 2
        return dummy.next


    def merge(self, l1, l2):
        head = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return head.next
    '''
    分治法自顶向下递归分裂链表，排序合并
    时间复杂度O（nlogn)空间复杂度O（N）
    '''
    # def sortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     return self.divide(head)
    #
    # def divide(self, head):
    #     if head is None or head.next is None:
    #         return head
    #
    #     fast, slow = head, head
    #     while fast.next and fast.next.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     head2 = slow.next
    #     slow.next = None
    #     h1 = self.divide(head)
    #     h2 = self.divide(head2)
    #     return self.merge(h1, h2)
    #


l = make_linkedlist([4,2,1,3])
show_linkedlist(Solution().sortList(l))