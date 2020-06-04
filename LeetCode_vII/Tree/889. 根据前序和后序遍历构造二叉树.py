## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
返回与给定的前序和后序遍历匹配的任何二叉树。
'''

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        index = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1: index + 1], post[:index])
        root.right = self.constructFromPrePost(pre[index + 1:], post[index:-1])
        return root


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
Solution().constructFromPrePost(pre, post)