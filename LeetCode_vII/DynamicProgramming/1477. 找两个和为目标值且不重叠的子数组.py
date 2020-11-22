# written by xiongbiao
# date - 2020-11-21

'''
给你一个整数数组 arr 和一个整数值 target 。
请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。
'''

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        length = len(arr) + 1
        dp = [float('inf')] * len(arr)

        ans = length
        pre = {}
        pre[0] = -1
        total = 0
        for i, a in enumerate(arr):
            total += a
            dp[i] = dp[i - 1]
            if total - target in pre:
                cur = i - pre[total - target]
                if pre[total - target] >= 0 and dp[pre[total - target]] != float("inf"):
                    ans = min(ans, cur + dp[pre[total - target]])
                dp[i] = min(dp[i-1], cur)
            pre[total] = i
            print('--------------')
            print('total:', total)
            print('dp:', dp)
            print('pre:', pre)
            print('ans:',ans)
            print('--------------')

        return -1 if ans == length else ans

print(Solution().minSumOfLengths([3,1,1,1,5,1,2,1], 3))