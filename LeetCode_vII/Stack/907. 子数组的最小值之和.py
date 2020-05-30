## written by xiongbiao
## date 2020-5-30
'''
给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
'''
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        stack = []
        sums, ans = 0, 0
        for n in A:
            count = 1
            while stack and n <= stack[-1][0]:
                val, cnt = stack.pop()
                count += cnt
                sums -= val * cnt
            stack.append((n, count))
            sums += count * n
            ans += sums
            ans %= mod
        # print(stack)

        return ans
print(Solution().sumSubarrayMins([3,1,2,4]))