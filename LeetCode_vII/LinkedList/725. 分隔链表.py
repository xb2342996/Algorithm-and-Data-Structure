## written by xiongbiao
## date 2020-5-26

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

class Solution(object):

    '''
    拆分链表，链表每次拆除一部分，cur节点已经指向下一个node
    时间复杂度O（N）空间复杂度O（k）
    '''
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        size = 0
        while node:
            size += 1
            node = node.next

        length = size // k
        rest = size % k
        parts = []
        cur = root
        for _ in range(k):
            head = cur
            count = length
            if rest > 0:
                count += 1
                rest -= 1
            for _ in range(count - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            parts.append(head)

        return parts


l = make_linkedlist([1,2,3])
nodes = Solution().splitListToParts(l, 5)
print(nodes)