"""
@author: xiongbiao
@date: 2021-04-23 21:27
"""

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def checkRow(i, j, grid):
            last = -1
            for p in range(i, i + 3):
                sum = 0
                for q in range(3):
                    sum += grid[p][q]
                if last != -1 and last != sum:
                    return False, None
                last = sum
            return True, last

        def checkCol(i, j, grid):
            last = -1
            for m in range(j, j + 3):
                sum = 0
                for n in range(3):
                    sum += grid[n][m]
                if last != -1 and last != sum:
                    return False, None
                last = sum
            return True, last

        def checkDiagonal(i, j, grid):
            diag = 0
            for k in range(3):
                diag += grid[i + k][j + k]

            antiDiag = 0
            for l in range(3):
                antiDiag += grid[i + l][j + 2 - l]

            if diag == antiDiag:
                return True, diag
            else:
                return False, None


        row, col = len(grid) - 2, len(grid[0]) - 2
        for i in range(row):
            for j in range(col):
                # print(grid[i][j])
                checkRow(i, j, grid)
                checkCol(i, j, grid)
                checkDiagonal(i, j, grid)



Solution().numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])