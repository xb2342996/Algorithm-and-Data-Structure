## written by xiongbiao
## date 2020-5-27

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist
'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
'''
class Solution(object):
    '''
    需要四个指针，才能完成原地变换，
    奇数指针指向每个新添加的奇数
    偶数头指针指向固定的偶数头部
    偶数指针指向每个新拼接上的偶数
    节点指针遍历链表中的节点
    时间复杂度O（N）空间复杂度O（1）
    '''
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        even_head = head.next
        odd = head
        even = even_head
        node = even.next
        while node:
            next_odd = node.next.next if node.next else None
            even.next = node.next
            odd.next = node
            node.next = even_head
            odd = odd.next
            even = even.next
            node = next_odd

        return head


l = make_linkedlist([1,2,3,4,5])
show_linkedlist(Solution().oddEvenList(l))
