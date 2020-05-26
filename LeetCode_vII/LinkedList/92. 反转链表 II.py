## written by xiongbiao
## date 2020-5-26

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
'''
class Solution(object):

    '''
    找到要反转的位置的前一个节点，根据长度翻转部分链表
    时间复杂度O(N)，空间复杂度O（1）
    '''
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        count = 0
        while node and count != m - 1:
            node = node.next
            count += 1
        print(node.val)
        self.reverse(node, n - m)
        return dummy.next

    def reverse(self, prev, size):

        head = prev.next
        cur = head
        next = cur.next
        count = 0
        while cur and count != size:
            head.next = next.next
            next.next = cur
            cur = next
            next = head.next
            count += 1
        prev.next = cur

l = make_linkedlist([1,2])
show_linkedlist(Solution().reverseBetween(l, 1,2))


