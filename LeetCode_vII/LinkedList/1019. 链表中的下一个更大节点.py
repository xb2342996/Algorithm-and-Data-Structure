## written by xiongbiao
## date 2020-5-26

from LinkedList.node import ListNode, make_linkedlist, show_linkedlist

'''
给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。
每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.val，那么就有 j > i 且  node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0 。
返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。
注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5 。
'''

class Solution(object):
    '''
    单调栈，维护一个索引栈一个元素栈
    '''
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        location = []
        ans = []
        loc = -1
        node = head
        while node:
            loc += 1
            ans.append(0)
            print('ans', ans)
            while stack and stack[-1] < node.val:
                ans[location[-1]] = node.val
                print('ans', ans)
                stack.pop()
                location.pop()
                print('stack',stack)
                print('location',location)
            stack.append(node.val)
            location.append(loc)
            print('stack',stack)
            print('location',location)

            node = node.next
        return ans

l = make_linkedlist([1,7,5,1,9,2,5,1])
Solution().nextLargerNodes(l)