## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode

'''
给定二叉树，按垂序遍历返回其结点值。
对位于 (X, Y) 的每个结点而言，其左右子结点分别位于 (X-1, Y-1) 和 (X+1, Y-1)。
'''

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        queue = []
        queue.append((root, 0, 0))
        verticals = defaultdict(list)
        while queue:
            node, x, y = queue.pop(0)
            if node.left:
                queue.append((node.left, x-1, y-1))
            if node.right:
                queue.append((node.right, x+1, y-1))

            verticals[x].append(node.val)
        verticals.values()
        verticals = sorted(verticals, key=lambda x: x[0])

