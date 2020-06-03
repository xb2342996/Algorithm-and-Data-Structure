## written by xiongbiao
## date 2020-6-3

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        for node in arr:
            while stack and node >= stack[-1]:
                num = stack.pop()
                res += num * min(node, stack[-1])
            stack.append(node)

        while len(stack) > 1:
            num = stack.pop()
            res += num * stack[-1]
        return res
print(Solution().mctFromLeafValues([6,2,4]))