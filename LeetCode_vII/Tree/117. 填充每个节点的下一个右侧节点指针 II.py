## written by xiongbiao
## date 2020-6-2

'''
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
'''

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    '''
    O（1）空间复杂度解法：
    利用已经连接好的上一层next层序遍历上一层，讲该层的字节点的next指针连好，并保存下一层的最左节点
    '''
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        mostleft = root
        while mostleft:
            prev, cur = None, mostleft

            mostleft = None

            while cur:
                prev, mostleft = self.processChild(cur.left, prev, mostleft)
                prev, mostleft = self.processChild(cur.right, prev, mostleft)
                cur = cur.next
        return root

    def processChild(self, node, prev, mostleft):
        if node:
            if prev:
                prev.next = node
            else:
                mostleft = node
            prev = node
        return prev, mostleft

    '''
    O（N）空间复杂度解法：
    层序遍历并把层序遍历的每个节点连接起来
    '''
    # def connect(self, root):
    #     """
    #     :type root: Node
    #     :rtype: Node
    #     """
    #     if root is None:
    #         return None
    #     queue = []
    #     queue.append(root)
    #     count = 1
    #     prev = None
    #     while queue:
    #         node = queue.pop(0)
    #         count -= 1
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #
    #         if count == 0:
    #             count = len(queue)
    #             prev = None
    #         else:
    #             if prev:
    #                 prev.next = node
    #             prev = node
    #     return root