"""
@author: xiongbiao
@date: 2022-03-03 23:28
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def dfs(num, first, second):
            print(first, second)
            if not num:
                return True
            res = first + second
            size = len(str(res))
            if num[:size] == str(res):
                return dfs(num[size:], second, res)
            return False

        for i in range(1, len(num)-1):
            if num[0] == '0' and i > 1: break
            for j in range(i + 1, len(num)):
                if num[i] == '0' and j - i > 1: break
                if dfs(num[j:], int(num[:i]), int(num[i:j])):
                    return True

        return False

print(Solution().isAdditiveNumber("112358"))


