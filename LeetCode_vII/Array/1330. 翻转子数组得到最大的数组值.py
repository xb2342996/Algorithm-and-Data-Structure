## written by xiongbiao
## date 2020-5-28

'''
给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。
你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。
请你找到可行的最大 数组值 。
'''

class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = float('-inf')
        ori_ans = 0
        for i in range(1, n):
            ori_ans += abs(nums[i] - nums[i-1])

        for r in range(1, n-1):
            delta = abs(nums[0] - nums[r + 1]) - abs(nums[r] - nums[r + 1])
            ans = max(ans, ori_ans + delta)

        for l in range(1, n-1):
            delta = abs(nums[n - 1] - nums[l - 1]) - abs(nums[l] - nums[l - 1])
            ans = max(ans, delta + ori_ans)

        f1, f2, f3, f4 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
        for l in range(1, n):
            abs_val = abs(nums[l] - nums[l - 1])
            f1 = max(f1, nums[l] + nums[l - 1] - abs_val)
            f2 = max(f2, -nums[l] + nums[l - 1] - abs_val)
            f3 = max(f3, nums[l] - nums[l - 1] - abs_val)
            f4 = max(f4, -nums[l] - nums[l - 1] - abs_val)

        g1, g2, g3, g4 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
        for r in range(n - 1):
            abs_val = abs(nums[r] - nums[r + 1])
            g1 = max(g1, -nums[r] - nums[r + 1] - abs_val)
            g2 = max(g2, -nums[r] + nums[r + 1] - abs_val)
            g3 = max(g3, nums[r] - nums[r + 1] - abs_val)
            g4 = max(g4, nums[r] + nums[r + 1] - abs_val)

        delta = max(f1+g1, g2+f2, g3+f3, g4+f4)
        return max(ans, ori_ans + delta)
print(Solution().maxValueAfterReverse([2,3,1,5,4]))
