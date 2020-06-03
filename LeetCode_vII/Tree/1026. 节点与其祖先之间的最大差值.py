## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。
'''
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diff = 0
        def dfs(node, min_val, max_val):
            if node is None:
                return
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            self.diff = max(abs(min_val - node.val), abs(max_val - node.val), self.diff)
            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return self.diff
