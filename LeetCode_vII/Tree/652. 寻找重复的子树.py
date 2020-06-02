## written by xiongbiao
## date 2020-6-2

from Tree.node import TreeNode
'''
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
两棵树重复是指它们具有相同的结构以及相同的结点值。
'''

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        from collections import defaultdict, Counter
        trees = defaultdict()
        trees.default_factory = trees.__len__
        count = Counter()
        ans = []
        print(trees)
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)

                return uid
        lookup(root)
        return ans
