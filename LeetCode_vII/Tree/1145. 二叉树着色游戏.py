## written by xiongbiao
## date 2020-6-1

from Tree.node import TreeNode
'''
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。
游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，
「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；
「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。
「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。
之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。
如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。
若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌。
'''
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.total_left = 0
        self.total_right = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == x:
                self.total_left = left
                self.total_right = right
            return 1 + left + right

        dfs(root)
        total_parent = n - self.total_left - self.total_right - 1
        for num in [total_parent, self.total_left, self.total_right]:
            if num > (n >> 1):
                return True
        return False