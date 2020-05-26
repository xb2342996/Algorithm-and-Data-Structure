## written by xiongbiao
## date 2020-5-26

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的 深拷贝。 
我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
'''
class Solution(object):

    def __init__(self):
        self.visited = {}
    '''
    遍历链表，复制一份新节点插在原节点后面，再次遍历链表将复制节点的随机索引连接上，将复制的节点从链表中拆出来拼上
    时间复杂度O（N）空间复杂度O（1）
    '''
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        node = head
        while node:
            new_node = Node(node.val, node.next, None)
            node.next = new_node
            node = new_node.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        original = head
        copy = head.next
        ori_head = copy
        while copy:
            original.next = copy.next
            if original.next:
                copy.next = original.next.next
            else:
                copy.next = None
            original = original.next
            copy = copy.next

        return ori_head

    # '''
    # 递归创建并保存节点，如果节点在保存表内直接返回节点，如果不在创建节点，继续递归
    # '''
    # def copyRandomList(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """
    #     if head is None:
    #         return None
    #
    #     if head in self.visited:
    #         return self.visited[head]
    #
    #     node = Node(head.val, None, None)
    #     self.visited[head] = node
    #
    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)
    #
    #     return node

    # '''
    # 2次遍历链表，第一次复制节点的next，保存每个节点到字典中，第二次复制random节点
    # 时间复杂度O（N）空间复杂度O（N）
    # '''''
    # def copyRandomList(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """
    #     if head is None:
    #         return None
    #     nodes = {}
    #
    #     new_node = Node(head.val, None, None)
    #     nodes[head] = new_node
    #     new_head = new_node
    #     cur = head.next
    #     while cur:
    #         node = Node(cur.val, None, None)
    #         new_node.next = node
    #         nodes[cur] = node
    #         cur = cur.next
    #         new_node = new_node.next
    #
    #     node = head
    #     new_node = new_head
    #
    #     while node:
    #         if node.random:
    #             random_node = nodes[node.random]
    #             new_node.random = random_node
    #         node = node.next
    #         new_node = new_node.next
    #     return new_head


