## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode
'''
我们从二叉树的根节点 root 开始进行深度优先搜索。
如果节点只有一个子节点，那么保证该子节点为左子节点。
给出遍历输出 S，还原树并返回其根节点 root。
'''
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        from collections import defaultdict
        S = list(S)
        num = 0
        while len(S) > 0:
            c = S.pop(0)
            num = num * 10 + int(c)
            if S[0] == '-':
                break


        root = TreeNode(num)
        levels = defaultdict(list)
        levels[0] = [root]

        num = 0
        level = 0
        while len(S) > 0:
            c = S.pop(0)
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '-':
                if num != 0:
                    node = TreeNode(num)
                    parent = levels[level-1][-1]
                    if not parent.left:
                        parent.left = node
                    else:
                        parent.right = node
                    levels[level].append(node)
                    num = 0
                    level = 0
                level += 1
        node = TreeNode(num)
        parent = levels[level - 1][-1]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
        return root

Solution().recoverFromPreorder('1-2--3--4-5--6--7')
