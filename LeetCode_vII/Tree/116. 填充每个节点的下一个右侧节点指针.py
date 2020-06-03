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
        leftmost = root
        while leftmost:
            cur, prev = leftmost, None
            while cur:
                prev, leftmost = self.connectChild(cur.left, prev, leftmost)
                prev, leftmost = self.connectChild(cur.right, prev, leftmost)
                cur = cur.next
        return root

    def connectChild(self, child, prev, leftmost):
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child
            prev = child
        return prev, leftmost

