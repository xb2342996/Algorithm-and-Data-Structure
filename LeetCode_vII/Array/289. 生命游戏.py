"""
@author: xiongbiao
@date: 2021-04-27 21:15
"""
'''
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
'''
'''
辅助数组：更新辅助数组，保持原数组，迭代结束后，将辅助数组复制过去
原地替换：需要用某些特定的值表示原始值，再将特定值刷新会变更后的值。
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def checkAlive(board, r, l):
            if abs(board[r][l]) == 1:
                return 1
            else:
                return 0

        def isAlive(i, j, m, n, board):
            top, bottom = i - 1, i + 1
            left, right = j - 1, j + 1
            count = 0

            if top >= 0:
                if left >= 0:
                    count += checkAlive(board, top, left)
                if right < n:
                    count += checkAlive(board, top, right)
                count += checkAlive(board, top, j)

            if left >= 0:
                count += checkAlive(board, i, left)

            if right < n:
                count += checkAlive(board, i, right)

            if bottom < m:
                if left >= 0:
                    count += checkAlive(board, bottom, left)
                if right < n:
                    count += checkAlive(board, bottom, right)
                count += checkAlive(board, bottom, j)

            if abs(board[i][j] == 1):
                if count < 2:
                    return -1
                if count > 3:
                    return -1
            if board[i][j] == 0 and count == 3:
                return -2

            return board[i][j]


        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                board[i][j] = isAlive(i, j, m, n, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == -2:
                    board[i][j] = 1


Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])