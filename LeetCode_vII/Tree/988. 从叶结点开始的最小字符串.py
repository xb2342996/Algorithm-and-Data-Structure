## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode

'''
给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。
找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
'''

class Solution(object):
    def smallestFromLeaf(self):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.ans = [[25, 1, 1], [25, 1, 3], [25, 3, 0], [25, 3, 2]]
        path = []
        # self.dfs(root, path)
        for i, path in enumerate(self.ans):
            self.ans[i] = ''.join([chr(p + 97) for p in path][::-1])
        return self.ans[0]

    def dfs(self, node, path):
        if node.left is None and node.right is None:
            path.append(node.val)
            self.ans.append(path[:])
            return
        path.append(node.val)
        if node.left:
            self.dfs(node.left, path)
            path.pop()
        if node.right:
            self.dfs(node.right, path)
            path.pop()

Solution().smallestFromLeaf()