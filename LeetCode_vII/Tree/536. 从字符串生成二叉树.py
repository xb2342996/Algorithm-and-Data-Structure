## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode

'''
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
'''

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        s = list(s)
        stack = []
        num = None
        sign = 1
        while len(s) > 0:
            c = s.pop(0)
            if c == '-':
                sign = -1
            if c.isdigit():
                if num is not None:
                    num = num * 10 + sign * int(c)
                else:
                    num = sign * int(c)
            if c == '(':
                if num is not None:
                    self.appendNode(num, stack)
                num = None
                sign = 1
            if c == ')':
                if num is not None:
                    self.appendNode(num, stack)
                stack.pop()
                num = None
                sign = 1
        return stack[-1] if stack else TreeNode(num)

    def appendNode(self, num, stack):
        new_node = TreeNode(num)
        if stack:
            node = stack[-1]
            if node.left is None:
                node.left = new_node
            else:
                node.right = new_node
        stack.append(new_node)

print('0'.isdigit())