## written by xiongbiao
## date 2020-5-30
'''
给定一个整数数组 A，返回满足下面条件的 非空、连续 子数组的数目：
子数组中，最左侧的元素不大于其他元素。
'''
class Solution(object):
    '''
    单调栈，栈内元素单调递增，如果当前元素>栈顶元素，将元素出栈，当前索引-弹出元素索引为弹出元素在其位置的子数组数量
    '''
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i, n in enumerate(nums):
            while len(stack) > 0 and n < nums[stack[-1]]:
                ans += i - stack.pop()
            stack.append(i)
        while len(stack) > 0:
            ans += len(nums) - stack.pop()
        return ans

print(Solution().validSubarrays([1,4,2,5,3]))