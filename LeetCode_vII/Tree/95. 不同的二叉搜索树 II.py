## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            if start > end:
                return [None,]
            trees = []
            for i in range(start, end + 1):
                left = generate(start, i-1)
                right = generate(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees
        return generate(1, n) if n else []

